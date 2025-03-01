*for odoo18*
# Description
This module serves as a basic template for implementing role-based views in Odoo. It allows you to customize the user interface according to the assigned role or function, showing or hiding information based on group settings. You can use and extend this template to suit specific needs of your business or application.

## Replication and Extension
To replicate this behavior in other cases:

- Add new fields:
Extend the model (e.g. res.partner) and add the desired fields.

- Create security groups:
Define new groups in the security XML file and make sure to reference them correctly (use the full XML ID).

- Modify Views:
Create inherited views using XPath to insert the new fields in the desired position. Restrict visibility using the groups attribute on each <field>.

- Update the Manifest:
Make sure all files (models, security and views) are included in the __manifest__.py.
