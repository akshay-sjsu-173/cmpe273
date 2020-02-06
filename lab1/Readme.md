This lab demonstrates a comparison between asynchronous and synchronous methods.

- For lightweight operations with smaller datasets, synchronous operations tend to give a better performance.
- With increase in processing steps or data volume, asynchronous operations tend to save a lot of time by
  executing co-routines concurrently.
- In the above scripts, a sleep/delay of 1 second is introduced in order to exemplify a strenous/lengthy task 
  as part of the function call. This enables us to display the proficiency of asynchronous method over synchronous
