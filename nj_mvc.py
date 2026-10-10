"""Find the soonest NJ MVC appointment by reading the public appointment wizard pages."""
from datetime import date, datetime
from typing import List, Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "https://telegov.njportal.com/njmvc/AppointmentWizard"
APPOINTMENT_TYPES = {
    "Initial permit (before knowledge test)": 15,
    "Knowledge test": 19,
}
NO_APPOINTMENTS = "No Appointments Available"


def wizard_url(type_id: int) -> str:
    return f"{BASE_URL}/{type_id}"


def headless_chrome() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    for arg in ("--headless=new", "--no-sandbox", "--disable-dev-shm-usage"):
        options.add_argument(arg)
    return webdriver.Chrome(options=options)


def parse_date_text(text: str) -> date:
    """'Next Available: 10/22/2026 08:30 AM' style text -> date (first m/d/Y token)."""
    for token in text.split():
        try:
            return datetime.strptime(token, "%m/%d/%Y").date()
        except ValueError:
            continue
    raise ValueError(f"no date in {text!r}")


def nearest_appointments(type_id: int, today: date | None = None) -> Tuple[int, List[str]]:
    """Return (days until the soonest appointment, locations offering it).

    Raises LookupError when no location has availability.
    """
    today = today or date.today()
    driver = headless_chrome()
    try:
        driver.get(wizard_url(type_id))
        names = [e.text.split("\n")[0] for e in driver.find_elements(By.XPATH, "//*[contains(@style,'font-weight:bold;')]")]
        texts = [e.text for e in driver.find_elements(By.XPATH, "//*[contains(@id, 'dateText')]")]
    finally:
        driver.quit()

    days = {name: (parse_date_text(t) - today).days for name, t in zip(names, texts) if t != NO_APPOINTMENTS}
    if not days:
        raise LookupError("no appointments available")
    soonest = min(days.values())
    return soonest, [name for name, d in days.items() if d == soonest]
