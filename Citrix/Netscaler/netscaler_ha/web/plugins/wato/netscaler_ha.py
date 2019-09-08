#######################################################
#
# Editor: Michiel van Pouderoijen
#
# Changelog:
#
# 2019.09.06:
# - Added this parameter rule for wato.
#   Gives the possibility to define the preferred HA-state of a
#   netscaler node trough the WATO interfaces.
#   When you define the preferred state, the check will change to warning
#   when running in the wrong state.
#   If not configured, the check will show a warning when part of a HA cluster
#
#######################################################
register_check_parameters(
    subgroup_applications,
    "netscaler_ha",
    _("Citrix Netscaler node state (HA)"),
    Dictionary(
        elements = [
            ("netscaler_ha_node_state",
                DropdownChoice(
                    title = _("Netscaler node state (HA)"),
                    help = _("Configure the preferred state of the Netscaler node. This way the HA state "
                              "can be checked and will change state when not running in the preferred state."),
                    choices = [
                        ( '0', _("Standalone node") ),
                        ( '1', _("Primary node") ),
                        ( '2', _("Secondary node") ),
                    ]
                )
            ),
        ]
    ),
    None,
    match_type = "dict",
)
