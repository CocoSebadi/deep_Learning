import streamlit as st
import pandas as pd
from datetime import datetime

# Function to validate employee number
def validate_employee_number(employee_number):
    valid_employee_numbers = ["emp123", "emp456", "emp789"]
    return employee_number in valid_employee_numbers

# Function to send email (you need to implement this)
def send_email(recipient, subject, body):
    # Implement your email sending logic here
    pass

# Function to update existing issue in DataFrame
def update_existing_issue(df, issue_id, new_data):
    # Implement your logic to update the existing issue in the DataFrame
    # For example, you can use pandas' loc function to locate the row by issue_id and update its values
    df.loc[df['Issue ID'] == issue_id, new_data.keys()] = new_data.values()

# Login Section
employee_number = st.text_input("Employee Number", max_chars=7)

if st.button("Login"):
    if len(employee_number) == 7 and validate_employee_number(employee_number):
        st.success("Login successful!")

        st.title("Project Issues Form")

        # Assuming you want to proceed with the issues form only after successful login
        if st.button("Proceed to Issues Form"):
            issue_action = st.radio("Select an action:", ["Update an Existing Issue"])

            if issue_action == "Update an Existing Issue":
                st.write("You chose to update an existing issue.")
                st.subheader("Consolidated Open Issues:")
                uploaded_file = st.file_uploader("Upload an existing issues tracker file", type=["csv", "xlsx"])

                if uploaded_file is not None:
                    # Read the uploaded file into a DataFrame
                    existing_issues_df = pd.read_csv(uploaded_file)  # Adjust the reading logic based on the file type
                    st.write("Existing Issues Tracker Loaded:")
                    st.write(existing_issues_df)

                    # Allow the user to select the issue they want to update
                    selected_issue_id = st.selectbox("Select the Issue to Update", existing_issues_df['Issue ID'])

                    # Additional form elements for updating an existing issue
                    issue_owner = st.text_input("Issue Owner")
                    original_date = st.date_input("Original Date")
                    revised_due_date = st.date_input("Revised Due Date")

                    # File attachment or written evidence for the update
                    attachment = st.file_uploader("Attach a File or Provide Written Evidence", type=["pdf", "docx"])

                    # Add a button to submit the form
                    if st.button("Submit"):
                        # Update logic
                        new_data = {
                            'Issue Owner': issue_owner,
                            'Original Date': original_date,
                            'Revised Due Date': revised_due_date
                            # Add other columns as needed
                        }

                        update_existing_issue(existing_issues_df, selected_issue_id, new_data)

                        # Display updated DataFrame
                        st.write("Updated Issues Tracker:")
                        st.write(existing_issues_df)
                        st.success("Form submitted successfully!")
                else:
                    st.warning("Please upload an existing issues tracker file.")
            else:
                st.error("Invalid action selected.")
        else:
            st.error("Login failed. Please try again.")
    else:
        st.error("Invalid employee number. Please try again.")
