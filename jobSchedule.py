#Method 1
def greedy_job_scheduling(jobs):
    # Sort the jobs based on their finish times
    jobs.sort(key=lambda x: x[1])
    n = len(jobs)
    schedule = []

    # Initialize the current time
    current_time = 0

    for i, job in enumerate(jobs):
        start_time, finish_time = job
        if start_time >= current_time:
            # If the job can be scheduled without overlap, schedule it
            schedule.append((i+1, start_time, finish_time))
            current_time = finish_time

    return schedule

def main():
    jobs = []
    num_jobs = int(input("Enter the number of jobs: "))
    for i in range(num_jobs):
        start_time = int(input(f"Enter start time for job {i+1}: "))
        finish_time = int(input(f"Enter finish time for job {i+1}: "))
        jobs.append((start_time, finish_time))

    schedule = greedy_job_scheduling(jobs)
    print("\nOptimized Schedule:")
    for job in schedule:
        print("Job", job[0], ":", job[1], "-", job[2])

main()


#Method 2 SJF
def sjf_job_scheduling():
    jobs = []

    # Input jobs from the user
    while True:
        job_name = input("Enter job name (press Enter to stop): ")
        if not job_name:
            break
        start_time = int(input("Enter start time of the job: "))
        burst_time = int(input("Enter burst time of the job: "))
        jobs.append((job_name, start_time, burst_time))

    # Sort jobs by start time
    jobs.sort(key=lambda x: x[1])

    current_time = int(jobs[0][1])  # Set current time to the start time of the first job
    final_schedule = []  # To store the final schedule of jobs

    while jobs:
        arrived_jobs = [job for job in jobs if int(job[1]) <= current_time]
        if arrived_jobs:
            # Select the job with the shortest burst time among the arrived jobs
            selected_job = min(arrived_jobs, key=lambda x: x[2])
            final_schedule.append(selected_job)
            jobs.remove(selected_job)
            current_time += selected_job[2]  # Update current time to the end time of the executed job
        else:
            # No jobs have arrived at the current time, move to the next job
            current_time = int(jobs[0][1])

    return final_schedule

# Example usage:
scheduled_jobs = sjf_job_scheduling()
print("Final Schedule of Jobs:")
for job in scheduled_jobs:
    print(job)
