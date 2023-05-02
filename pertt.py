import streamlit as st
import numpy as np

def pert_analysis():
    st.title("PERT Analysis")

    st.header("Enter tasks and time estimates")
    tasks = st.text_area("Tasks (one per line)")
    optimistic_times = st.text_area("Optimistic Time Estimates (in days, one per line)")
    most_likely_times = st.text_area("Most Likely Time Estimates (in days, one per line)")
    pessimistic_times = st.text_area("Pessimistic Time Estimates (in days, one per line)")

    if st.button("Calculate Expected Time and Variance"):
        tasks = tasks.split("\n")
        optimistic_times = list(map(float, optimistic_times.split("\n")))
        most_likely_times = list(map(float, most_likely_times.split("\n")))
        pessimistic_times = list(map(float, pessimistic_times.split("\n")))

        expected_times = []
        variances = []
        std_deviations = []

        for i in range(len(tasks)):
            optimistic_time = optimistic_times[i]
            most_likely_time = most_likely_times[i]
            pessimistic_time = pessimistic_times[i]

            expected_time = (optimistic_time + 4 * most_likely_time + pessimistic_time) / 6
            variance = ((pessimistic_time - optimistic_time) / 6) ** 2
            std_deviation = np.sqrt(variance)

            expected_times.append(expected_time)
            variances.append(variance)
            std_deviations.append(std_deviation)

        st.header("Expected Time Estimates")
        for i in range(len(tasks)):
            st.write(tasks[i] + ": " + str(expected_times[i]))

        st.header("Variance Estimates")
        for i in range(len(tasks)):
            st.write(tasks[i] + ": " + str(variances[i]))

        st.header("Standard Deviation")
        for i in range(len(tasks)):
            st.write(tasks[i] + ": " + str(std_deviations[i]))

        st.header("Expected Duration")
        expected_duration = sum(expected_times)
        st.write(expected_duration)

        # Find the critical path
        max_duration = max(expected_times)
        critical_path = []
        for i in range(len(tasks)):
            if expected_times[i] == max_duration:
                critical_path.append(tasks[i])

        st.header("Critical Path")
        st.write(critical_path)

if __name__ == "__main__":
    pert_analysis()
