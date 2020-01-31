#  Single-tank Water Tank

This case study is builds on a single-tank water tank pilot study of the
INTO-CPS Project, which is available at
https://github.com/INTO-CPS-Association/example-single_watertank. 

This case study was created to demonstrate how to incorporate an external data
supplier into an FMI co-simulation via an External Data Broker (EDB) FMU. The
realisation of EDB FMU in this case study is RabbitMQ FMU. See
https://github.com/INTO-CPS-Association/rabbitmq-fmu-documentation/releases for
more information on EDB and RabbitMQ FMU along with its relation to this
example.

## Overview

The single-tank water tank pilot study is a simple example that comprises a single water tank which is controlled by a cyber controller. The tank has a constant inflow of water and when the water level of the tank reaches a particular maximum level (defined in the controller) the controller sends a command to the tank to empty using an exit valve. When the water level reaches a particular minimum level (defiend in the controller) the controller sends a command to the tank to close the exit valve.

![Single-tank Water Tank](resources/watertank.png)

This case study combines the pilot study with an external data supplier that
supplies historic water level data. RabbitMQ is used to bring this historic
water level data into an FMI context, such that both the modelled water level
data and the historic water level data is available in the same co-simulation.

The following must be carried out, in the order specified, to execute the co-simulation:
1.  Start the RabbitMQ server. See `readme.md` within
    `resources/external_data_supplier`.
2.  Start the co-simulation by loading the project into the INTO-CPS
    Application.
3.  Run the python3 script Publish.py within `resources/external_data_supplier`.
