import createPushNotificationsJobs from './8-job';
import { kue } from 'redis';

const queue = kue.createQueue();

queue.testMode.enter();

beforeEach(() => {
  queue.testMode.clear();
});

test('createPushNotificationsJobs', () => {
  const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    },
  ];

  createPushNotificationsJobs(jobs, queue);

  expect(queue.testMode.jobs.length).toBe(1);
  expect(queue.testMode.jobs[0].type).toBe('push_notification_code_3');
  expect(queue.testMode.jobs[0].data).toStrictEqual(jobs[0]);
});

test('createPushNotificationsJobs: jobs is not an array', () => {
  expect(() => createPushNotificationsJobs({}, queue)).toThrowError(
    'Jobs is not an array'
  );
});

test('createPushNotificationsJobs: jobs is not an array', () => {
  expect(() => createPushNotificationsJobs('hello', queue)).toThrowError(
    'Jobs is not an array'
  );
});

test('createPushNotificationsJobs: jobs is not an array', () => {
  expect(() => createPushNotificationsJobs(123, queue)).toThrowError(
    'Jobs is not an array'
  );
});

test('createPushNotificationsJobs: jobs is not an array', () => {
  expect(() => createPushNotificationsJobs(null, queue)).toThrowError(
    'Jobs is not an array'
  );
});

test('createPushNotificationsJobs: jobs is not an array', () => {
  expect(() => createPushNotificationsJobs(undefined, queue)).toThrowError(
    'Jobs is not an array'
  );
});

test('createPushNotificationsJobs: jobs is not an array', () => {
  expect(() => createPushNotificationsJobs(true, queue)).toThrowError(
    'Jobs is not an array'
  );
});

test('createPushNotificationsJobs: jobs is not an array', () => {
  expect(() => createPushNotificationsJobs(false, queue)).toThrowError(
    'Jobs is not an array'
  );
});

test('createPushNotificationsJobs: jobs is not an array', () => {
  expect(() => createPushNotificationsJobs(() => {}, queue)).toThrowError(
    'Jobs is not an array'
  );
});

test('createPushNotificationsJobs: jobs is not an array', () => {
  expect(() => createPushNotificationsJobs(Symbol('test'), queue)).toThrowError(
    'Jobs is not an array'
  );
});
