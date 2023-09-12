import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.title('Total Experience Calculator')

start_date = st.date_input('Start Date')
end_date = st.date_input('End Date', datetime.today())

if start_date and end_date:

    if start_date > end_date:
        st.warning('End Date should be after the Start Date.')
    else:
        delta = relativedelta(end_date, start_date)
        years = delta.years
        months = delta.months
        days = delta.days
        st.write(f'Your total experience is: {years} years, {months} months, and {days} days.')

