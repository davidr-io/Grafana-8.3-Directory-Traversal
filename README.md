### CVE-2021-43798 Python script

#### Description: Grafana 8.3.0 Directory Traversal (Try this is EDB-ID 50581 is not working!)

#### Original Article: https://ethicalhacking.uk/cve-2021-43798-dissecting-the-grafana-path-traversal-vulnerability/#gsc.tab=0

##### During a box in OffSec Proving Ground (Fanatastic), I encountered Grafana 8.3.0 and pretty quickly found exploitdb id 50581 but for some reason it was not working.
##### I found a working PoC on the above article that quickly allowed me to read /etc/passwd and proceed with attacking the box
##### I decided to build off the PoC so it would be a bit more interactive and allow for quick manual enumeration of files to read

