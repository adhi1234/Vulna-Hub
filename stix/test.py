from stix.core import STIXPackage 
from stix.report import Report
from stix.report.header import Header




stix_package=STIXPackage()
stix_report=Report()
stix_report.header=Header()
stix_report.header.description="Getting Started"
stix_package.add(stix_report)

print(stix_package.to_xml())