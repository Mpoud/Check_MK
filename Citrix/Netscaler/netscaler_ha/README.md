# Netscaler HA node state check 1.0
The original netscaler_ha check is always in OK state. With this version, you can define the preferred state of the Netscaler node (through WATO). When the current state is not the preferred state, the check will result in WARNING.
