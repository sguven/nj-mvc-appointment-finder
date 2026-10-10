"""Streamlit app: how many days until the soonest NJ MVC appointment, and where."""
from datetime import date
from pathlib import Path

import streamlit as st

from nj_mvc import APPOINTMENT_TYPES, nearest_appointments, wizard_url

st.title("NJ MVC Appointment Finder")
st.caption(f"Today is {date.today():%A, %B %d, %Y}. Pick an appointment type to find the soonest open slot.")

for label, type_id in APPOINTMENT_TYPES.items():
    if st.button(label, use_container_width=True):
        with st.spinner("Checking every MVC location…"):
            try:
                days, places = nearest_appointments(type_id)
                st.markdown(f"## :red[{days} day(s)] to the nearest appointment")
                st.write("at " + ", ".join(places))
            except LookupError:
                st.warning("No appointments are available right now.")
            except Exception as exc:  # site layout changes, driver issues
                st.error(f"Could not read the MVC site: {exc}")
        st.link_button("Book on the MVC site", wizard_url(type_id))

st.image(str(Path(__file__).parent / "assets" / "dmv.gif"))
