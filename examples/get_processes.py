"""Python interface to GenoLogics LIMS via its REST API.

Usage example: Get some processes.

NOTE: You need to set the BASEURI, USERNAME AND PASSWORD.

Per Kraulis, Science for Life Laboratory, Stockholm, Sweden.
"""

from genologics.lims import *

# Login parameters for connecting to a LIMS instance.
# NOTE: Modify according to your setup.
from genologics.site_cloud import BASEURI, USERNAME, PASSWORD

# Create the LIMS interface instance, and check the connection and version.
lims = Lims(BASEURI, USERNAME, PASSWORD)
lims.check_version()

# Get the list of all processes.
processes = lims.get_processes()
print len(processes), 'processes in total'

process = Process(lims, id='QCF-PJK-120703-24-1140')
print process, process.id, process.type, process.type.name
for input, output in process.input_output_maps:
    if input:
        print 'input:', input.items()
    if output:
        print 'output:', output.items()
