# NJ MVC Appointment Finder

Getting a New Jersey MVC appointment means clicking through every location to find the
earliest open slot. This project does that automatically: a headless Chrome reads the
public appointment wizard, compares every location's next available date and reports
how many days away the soonest appointment is, and where.

It comes in three forms:

| | What it does |
|---|---|
| `streamlit_app.py` | Web app – one button per appointment type, shows the soonest date and locations |
| `scripts/email_alert.py` | Emails you the result; run it daily with cron to watch for openings |
| `notebooks/colab_appointment_check.ipynb` | The same check in Google Colab, no local setup |

All three share the scraping logic in `nj_mvc.py`.

## Run it

```bash
pip install -r requirements.txt     # also needs Chrome/Chromium installed
streamlit run streamlit_app.py
```

On Streamlit Community Cloud, `packages.txt` installs Chromium and its driver.

For the email alert, create a [Gmail app password](https://support.google.com/accounts/answer/185833)
and set `GMAIL_USER`, `GMAIL_APP_PASSWORD` and optionally `ALERT_TO` before running
`python scripts/email_alert.py`.

## Note

Built in 2022 against the MVC site of the time. The page selectors in `nj_mvc.py`
may need updating if the wizard's layout has changed.
