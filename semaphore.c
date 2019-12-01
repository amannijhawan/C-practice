#include  <pthread.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
  pthread_cond_t cond;
  pthread_mutex_t mutex;
  volatile unsigned N;
} my_semaphore;

#define SEM_INIT(n)                    \
{                                      \
    .cond = PTHREAD_COND_INITIALIZER,  \
    .mutex = PTHREAD_MUTEX_INITIALIZER, \
    .N    = n                          \
};
/*
void sem_init(my_semaphore * sem, unsigned int N) {
  pthread_mutex_init(&sem->mutex, NULL);
  pthread_cond_init(&sem->cond, NULL);
  sem->N = N;
}
*/
void sem_acquire(my_semaphore * sem) {
  pthread_mutex_lock(&sem->mutex);
  while (sem->N == 0) {
    pthread_cond_wait(&sem->cond, &sem->mutex);
    }
  --(sem->N);
  pthread_mutex_unlock(&sem->mutex);
}

void sem_release(my_semaphore * sem) {
  pthread_mutex_lock(&sem->mutex);
  ++(sem->N);
  pthread_cond_signal(&sem->cond);
  pthread_mutex_unlock(&sem->mutex);
}

void sem_destroy(my_semaphore * sem) {
  pthread_cond_destroy(&sem->cond);
  pthread_mutex_destroy(&sem->mutex);
}

static const int N = 20;
static const int Z = 200000;
static int COUNTER = 0;

void *thread_func(void *semaphore) {
    my_semaphore * mumm = semaphore;

    sem_acquire(mumm);
    for(int i = 0; i < Z; i++) {
        ++COUNTER;
    }
    sem_release(mumm);
    return NULL;
}


int main(void) {
    my_semaphore Mumm = SEM_INIT(1);

    pthread_t threads[N];
    for(int i = 0; i < N; i++) {
        pthread_create(&threads[i],NULL,thread_func,&Mumm);
    }

    for(int i = 0; i < N; i++) {
        pthread_join(threads[i],NULL);
    }

    fprintf(stderr,"%d\n", COUNTER);
    return EXIT_SUCCESS;
}

