from src.schemas.sustainability import SustainabilityReport


def test_sustainability_report():

    report = SustainabilityReport(
        company_name="Future City Initiative",
        industry="Smart Infrastructure",
        country="United Kingdom",
        report_year=2026,
        revenue="£2.4 Billion",
        employees=8500,
        carbon_reduction_target="55% by 2035",
        net_zero_target=2045,
        renewable_energy_percentage=72.0,
    )

    assert report.company_name == "Future City Initiative"
    assert report.industry == "Smart Infrastructure"
    assert report.country == "United Kingdom"
    assert report.report_year == 2026
    assert report.employees == 8500
    assert report.net_zero_target == 2045
    assert report.renewable_energy_percentage == 72.0