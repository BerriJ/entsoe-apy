from enum import Enum

__NAMESPACE__ = "urn:entsoe.eu:wgedi:codelists"


class AllocationModeTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Order by price with pro
        rata</Title> <Definition>The allocation method is by price with
        eventual pro rata.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Order by price with
        first come - first served</Title> <Definition>The allocation
        method is by price with eventual use of first come first
        served.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>First come - First
        served</Title> <Definition>The allocation method is first come
        first served.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Pro rata</Title>
        <Definition>The allocation method is pro rata.</Definition>
        </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"


class AnalogTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Flow</Title>
        <Definition>This is the computed flow for the monitored element
        in the constraint situation ("N situation", "N-1 situation" ...)
        after the capacity calculation. The flow is expressed in A, %,
        or MW.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Permanent admissible
        transmission limit (PATL)</Title> <Definition>The permanent load
        of transmission system elements which is allowed for an
        unlimited period and which does not cause physical damage to the
        transmission system elements as long as the defined threshold is
        respected.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Flow reliability
        margin</Title> <Definition>This is the flow reliability margin
        for a given critical network element. The amount of MW or A that
        is reserved for this critical network element and shall not be
        used for the computed outage situation, in order to secure the
        power network.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Spanning margin
        value</Title> <Definition>This is the margin that is taken into
        account when spanning (fall-back process) is applied. Spanning
        marginal value is an historical based parameter which specifies
        the amount of MW that reduces the RAM when spanning is
        applied.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Long term allocation
        margin</Title> <Definition>This is the amount of MW that is
        added to the capacity of the critical network element in order
        to automatically include the long term allocation domain into
        the flow based domain.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Final adjustment margin
        value</Title> <Definition>This is the margin that is manually
        added or subtracted to the capacity of the critical network
        element. A negative value for final adjustment value simulates
        the effect of an additional margin due to complex remedial
        actions (RA) which cannot be modeled and so calculated in the
        flow based parameter calculation. A positive value for FAV as a
        consequence of the verification phase of the flow based domain,
        leading to the need to reduce the margin on one or more CBs for
        system security reasons.</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Transitory admissible
        transmission limit (TATL)</Title> <Definition>The temporary
        overload of transmission system elements which is allowed for a
        limited period and which does not cause physical damage to the
        transmission system elements as long as the defined duration and
        thresholds are respected.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Long admissible
        flow</Title> <Definition>This is the value, expressed in A or
        MW, that the overload flow in a network element shall not exceed
        for a duration no longer than the long duration. The long
        duration value depends on the TSO network operating
        rules.</Definition> </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>Negative Final
        adjustment margin value</Title> <Definition>This is the margin
        that is manually added to the capacity of the critical network
        element in order to simulate the effect of an additional margin
        due to complex remedial actions (RA) which cannot be modeled and
        so calculated in the flow based parameter
        calculation.</Definition> </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Minimum voltage
        level</Title> <Definition>This is the minimum voltage that can
        be supported by a network element without involving a risk for
        the security of supply.</Definition> </CodeDescription>
    :cvar A11: <CodeDescription xmlns=""> <Title>Maximum voltage
        level</Title> <Definition>This is the maximum voltage that can
        be supported by a network element without involving a risk for
        the security of supply.</Definition> </CodeDescription>
    :cvar A12: <CodeDescription xmlns=""> <Title>TATL after automatic
        RA</Title> <Definition>The Transitory admissible transmission
        limit (TATL) which is allowed after an automatic Remedial Action
        (RA) has been applied.</Definition> </CodeDescription>
    :cvar A13: <CodeDescription xmlns=""> <Title>TATL after curative
        RA</Title> <Definition>The Transitory admissible transmission
        limit (TATL) which is allowed after a curative Remedial Action
        (RA) has been applied.</Definition> </CodeDescription>
    :cvar A14: <CodeDescription xmlns=""> <Title>Computed
        Voltage</Title> <Definition>This is the computed voltage for a
        given monitored element.</Definition> </CodeDescription>
    :cvar A15: <CodeDescription xmlns=""> <Title>Zero-Balance
        flow</Title> <Definition>This is the amount of power affected by
        a contingency that reflects a situation with a scheduled
        exchange of zero.</Definition> </CodeDescription>
    :cvar A16: <CodeDescription xmlns=""> <Title>Available margin after
        remedial actions</Title> <Definition>This is the available flow
        margin adjusted for the consideration of remedial actions in
        capacity calculation.</Definition> </CodeDescription>
    :cvar A17: <CodeDescription xmlns=""> <Title>Loss Factor</Title>
        <Definition>This is the loss factor for an asset.</Definition>
        </CodeDescription>
    :cvar A18: <CodeDescription xmlns=""> <Title>Adjustment for minimum
        RAM</Title> <Definition>This is the adjustment applied to the
        capacity of a branch to have a minimum RAM (Remaining Available
        Margin) available for commercial exchanges.</Definition>
        </CodeDescription>
    :cvar A19: <CodeDescription xmlns=""> <Title>Tap changer</Title>
        <Definition>The position of a Tap changer.</Definition>
        </CodeDescription>
    :cvar A20: <CodeDescription xmlns=""> <Title>Regulator mode</Title>
        <Definition>A measurement type indicating the control mode of a
        regulator, i.e. from voltage regulation to fixed MVAR
        regulation.</Definition> </CodeDescription>
    :cvar A21: <CodeDescription xmlns=""> <Title>Regulator set-
        point</Title> <Definition>The set-point of a regulator. A
        regulator can be a tap changer, a synchronous machine, a SVC or
        a shunt.</Definition> </CodeDescription>
    :cvar A22: <CodeDescription xmlns=""> <Title>Reference Flow</Title>
        <Definition>This is the amount of power affected by a
        contingency that reflects a situation with scheduled exchanges
        from a reference situation.</Definition> </CodeDescription>
    :cvar A23: <CodeDescription xmlns=""> <Title>CO2 emission</Title>
        <Definition>This is the CO2 emission from one or several
        assets.</Definition> </CodeDescription>
    :cvar A24: <CodeDescription xmlns=""> <Title>Maximum admissible
        current (Imax)</Title> <Definition>The maximum admissible
        current of a critical network element or a critical network
        element and contingency.</Definition> </CodeDescription>
    :cvar A25: <CodeDescription xmlns=""> <Title>Individual value
        adjustment (IVA)</Title> <Definition>Individual value adjustment
        resulting from TSO validation process. </Definition>
        </CodeDescription>
    :cvar A26: <CodeDescription xmlns=""> <Title>Linear flow
        approximation (F0)</Title> <Definition>The linear approximation
        of a flow in the reference net position in a situation without
        any cross-zonal exchanges.</Definition> </CodeDescription>
    :cvar A27: <CodeDescription xmlns=""> <Title>Flow without commercial
        exchanges (F0_Wce)</Title> <Definition>Flow per critical network
        element and contingency without commercial exchanges within a
        capacity calculation region.</Definition> </CodeDescription>
    :cvar A28: <CodeDescription xmlns=""> <Title>Flow without commercial
        exchanges between areas (F0_all)</Title> <Definition>Flow per
        critical network element and contingency without commercial
        exchanges between bidding zones within the same or different
        synchronous areas.</Definition> </CodeDescription>
    :cvar A29: <CodeDescription xmlns=""> <Title>Flow due to non-costly
        remedial actions (F_nrao)</Title> <Definition>Expected flow
        change due to non-costly remedial actions.</Definition>
        </CodeDescription>
    :cvar A30: <CodeDescription xmlns=""> <Title>Flow after long-term
        nominations (F_LTN)</Title> <Definition>Flow after consideration
        of long-term nominations.</Definition> </CodeDescription>
    :cvar A31: <CodeDescription xmlns=""> <Title>Coordinated value
        adjustment (CVA)</Title> <Definition>Coordinated value
        adjustment resulting from coordinated validation
        process.</Definition> </CodeDescription>
    :cvar A32: <CodeDescription xmlns=""> <Title>Minimum remaining
        available margin as ratio of maximum allowable power flow
        (Ramr)</Title> <Definition>Percentage of the maximum allowable
        power flow that needs to be available as minimum Remaining
        Available Margin. </Definition> </CodeDescription>
    :cvar A33: <CodeDescription xmlns=""> <Title>Flows from already
        allocated cross-zonal capacities (Faac)</Title>
        <Definition>Flows resulting from previously allocated cross-
        zonal capacities.</Definition> </CodeDescription>
    :cvar A34: <CodeDescription xmlns=""> <Title>Flow from remedial
        action (FRA)</Title> <Definition>Flow for increasing the
        Remaining Available Margin due to remedial action.</Definition>
        </CodeDescription>
    :cvar A35: <CodeDescription xmlns=""> <Title>Assumed external
        exchanges</Title> <Definition>Flow resulting from assumed
        commercial exchanges outside the region (F_uaf).</Definition>
        </CodeDescription>
    :cvar A36: <CodeDescription xmlns=""> <Title>Minimum remaining
        available margin target</Title> <Definition>Target capacity for
        exchanges by deducing the exchanges not related to the
        region.</Definition> </CodeDescription>
    :cvar A37: <CodeDescription xmlns=""> <Title>Average voltage</Title>
        <Definition>Average voltage on two connecting nodes of a
        critical network element resulting from AC load flow calculation
        with applied reactive power constraints (U).</Definition>
        </CodeDescription>
    :cvar A38: <CodeDescription xmlns=""> <Title>Average power
        factor</Title> <Definition>Average power factor on two
        connecting nodes of a critical network element resulting from AC
        load flow calculation (cos phi).</Definition> </CodeDescription>
    :cvar A39: <CodeDescription xmlns=""> <Title>Lower ramp rate</Title>
        <Definition>The maximum rate that the output can be lowered
        by.</Definition> </CodeDescription>
    :cvar A40: <CodeDescription xmlns=""> <Title>Raise ramp rate</Title>
        <Definition>The maximum rate that the output can be raised
        by.</Definition> </CodeDescription>
    :cvar A41: <CodeDescription xmlns=""> <Title>Negative reference
        flow</Title> <Definition>The amount of power negatively affected
        by a contingency that reflects a situation with scheduled
        exchanges from a reference situation. </Definition>
        </CodeDescription>
    :cvar A42: <CodeDescription xmlns=""> <Title>Negative flow due to
        non-costly remedial actions</Title> <Definition>Negative
        expected flow change due to non-costly remedial
        actions.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"
    A13 = "A13"
    A14 = "A14"
    A15 = "A15"
    A16 = "A16"
    A17 = "A17"
    A18 = "A18"
    A19 = "A19"
    A20 = "A20"
    A21 = "A21"
    A22 = "A22"
    A23 = "A23"
    A24 = "A24"
    A25 = "A25"
    A26 = "A26"
    A27 = "A27"
    A28 = "A28"
    A29 = "A29"
    A30 = "A30"
    A31 = "A31"
    A32 = "A32"
    A33 = "A33"
    A34 = "A34"
    A35 = "A35"
    A36 = "A36"
    A37 = "A37"
    A38 = "A38"
    A39 = "A39"
    A40 = "A40"
    A41 = "A41"
    A42 = "A42"


class AssetTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Tie line</Title>
        <Definition>A high voltage line used for cross border energy
        interconnections.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Line</Title>
        <Definition>A specific electric line within a
        country.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Resource Object</Title>
        <Definition>A resource that can either produce or consume
        energy.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Generation</Title>
        <Definition>A resource that can produce energy.</Definition>
        </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Load</Title>
        <Definition>A resource that can consume energy.</Definition>
        </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Phase Shift
        Transformer</Title> <Definition>An electrical device for
        controlling the power flow through specific lines in a power
        transmission network.</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Circuit Breaker</Title>
        <Definition>An electrical switch designed to protect an
        electrical circuit from damage caused by overcurrent/overload or
        short circuit.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Busbar</Title>
        <Definition>A specific element within a substation to connect
        grid elements for energy distribution purposes.</Definition>
        </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>Capacitor</Title>
        <Definition>A transmission element designed to inject reactive
        power into the transmission network. </Definition>
        </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Inductor</Title>
        <Definition>A transmission element designed to compensate
        reactive power in the transmission network.</Definition>
        </CodeDescription>
    :cvar A11: <CodeDescription xmlns=""> <Title>Power plant
        connection</Title> <Definition>All the network equipment that
        link the generating unit to the grid.</Definition>
        </CodeDescription>
    :cvar A12: <CodeDescription xmlns=""> <Title>FACTS</Title>
        <Definition>Flexible Alternating Current Transmission
        System</Definition> </CodeDescription>
    :cvar A13: <CodeDescription xmlns=""> <Title>Production unit</Title>
        <Definition>A production unit is a composition of one or several
        generation units.</Definition> </CodeDescription>
    :cvar A14: <CodeDescription xmlns=""> <Title>Internal tie
        line</Title> <Definition>An internal tie line is a line between
        two scheduling areas within the same bidding zone.</Definition>
        </CodeDescription>
    :cvar B01: <CodeDescription xmlns=""> <Title>Biomass</Title>
        <Definition>A resource using biomass for energy.</Definition>
        </CodeDescription>
    :cvar B02: <CodeDescription xmlns=""> <Title>Fossil Brown
        coal/Lignite</Title> <Definition>A resource using Fossil Brown
        coal/Lignite for energy.</Definition> </CodeDescription>
    :cvar B03: <CodeDescription xmlns=""> <Title>Fossil Coal-derived
        gas</Title> <Definition>A resource using Fossil Coal-derived gas
        for energy.</Definition> </CodeDescription>
    :cvar B04: <CodeDescription xmlns=""> <Title>Fossil Gas</Title>
        <Definition>A resource using Fossil Gas for energy.</Definition>
        </CodeDescription>
    :cvar B05: <CodeDescription xmlns=""> <Title>Fossil Hard
        coal</Title> <Definition>A resource using Fossil Hard coal for
        energy.</Definition> </CodeDescription>
    :cvar B06: <CodeDescription xmlns=""> <Title>Fossil Oil</Title>
        <Definition>A resource using Fossil Oil for energy.</Definition>
        </CodeDescription>
    :cvar B07: <CodeDescription xmlns=""> <Title>Fossil Oil
        shale</Title> <Definition>A resource using Fossil Oil shale for
        energy.</Definition> </CodeDescription>
    :cvar B08: <CodeDescription xmlns=""> <Title>Fossil Peat</Title>
        <Definition>A resource using Fossil Peat for
        energy.</Definition> </CodeDescription>
    :cvar B09: <CodeDescription xmlns=""> <Title>Geothermal</Title>
        <Definition>A resource using Geothermal for energy.</Definition>
        </CodeDescription>
    :cvar B10: <CodeDescription xmlns=""> <Title>Hydro-electric pure
        pumped storage head installation</Title> <Definition>Unit in
        which moving water energy is converted to electricity using
        flowing water to generate electricity with a large dam and
        reservoirs. Pure pumped storage plants store water in an upper
        reservoir with no natural inflows.</Definition>
        </CodeDescription>
    :cvar B11: <CodeDescription xmlns=""> <Title>Hydro Run-of-river head
        installation</Title> <Definition>Unit in which moving water
        energy is converted to electricity using flowing water to
        generate electricity in the absence of a large dam and
        reservoirs.</Definition> </CodeDescription>
    :cvar B12: <CodeDescription xmlns=""> <Title>Hydro-electric storage
        head installation</Title> <Definition>Unit in which moving water
        energy is converted to electricity using flowing water to
        generate electricity with a large dam and
        reservoirs.</Definition> </CodeDescription>
    :cvar B13: <CodeDescription xmlns=""> <Title>Marine
        unspecified</Title> <Definition>Unit in which marine energy is
        converted to electricity with equipment/devices not
        specified.</Definition> </CodeDescription>
    :cvar B14: <CodeDescription xmlns=""> <Title>Nuclear
        unspecified</Title> <Definition>A unit in which the heat source
        is a nuclear reactor of type that is not specified in other
        nuclear types. </Definition> </CodeDescription>
    :cvar B15: <CodeDescription xmlns=""> <Title>Other renewable</Title>
        <Definition>A resource using Other renewable for
        energy.</Definition> </CodeDescription>
    :cvar B16: <CodeDescription xmlns=""> <Title>Solar
        unspecified</Title> <Definition>Unit in which solar energy is
        converted to electricity with equipment/devices not
        specified.</Definition> </CodeDescription>
    :cvar B17: <CodeDescription xmlns=""> <Title>Waste</Title>
        <Definition>A resource using Waste for energy.</Definition>
        </CodeDescription>
    :cvar B18: <CodeDescription xmlns=""> <Title>Wind Offshore</Title>
        <Definition>Unit in which wind energy is converted to
        electricity using wind farms constructed in bodies of water,
        usually in the ocean.</Definition> </CodeDescription>
    :cvar B19: <CodeDescription xmlns=""> <Title>Wind Onshore</Title>
        <Definition>Unit in which wind energy is converted to
        electricity using wind farms constructed on land.</Definition>
        </CodeDescription>
    :cvar B20: <CodeDescription xmlns=""> <Title>Other
        unspecified</Title> <Definition>Other unspecified
        technology.</Definition> </CodeDescription>
    :cvar B21: <CodeDescription xmlns=""> <Title>AC Link</Title>
        <Definition>Overhead line or cable which is used to transmit
        electrical power via Alternative Current.</Definition>
        </CodeDescription>
    :cvar B22: <CodeDescription xmlns=""> <Title>DC Link</Title>
        <Definition>Overhead line or cable which is used to transmit
        electrical power via Direct Current.</Definition>
        </CodeDescription>
    :cvar B23: <CodeDescription xmlns=""> <Title>Substation</Title>
        <Definition>An assembly of equipment in an electric power system
        through which electric energy is passed for transmission,
        transformation, distribution or switching.</Definition>
        </CodeDescription>
    :cvar B24: <CodeDescription xmlns=""> <Title>Transformer</Title>
        <Definition>Electrical device that transfers energy from one
        voltage level to another voltage level.</Definition>
        </CodeDescription>
    :cvar B25: <CodeDescription xmlns=""> <Title>Energy storage</Title>
        <Definition>A resource that stores energy. It could be gas,
        electricity, etc.</Definition> </CodeDescription>
    :cvar B26: <CodeDescription xmlns=""> <Title>Demand Side
        Response</Title> <Definition>A resource that change its
        electricity consumption patterns in response to a signal or
        incentive.</Definition> </CodeDescription>
    :cvar B27: <CodeDescription xmlns=""> <Title>Dispatchable hydro
        resource</Title> <Definition>A resource referring to
        dispatchable hydro generation.</Definition> </CodeDescription>
    :cvar B28: <CodeDescription xmlns=""> <Title>Solar
        photovoltaic</Title> <Definition>Unit in which solar energy is
        converted to electricity using a technology based on the
        photoelectric effect.</Definition> </CodeDescription>
    :cvar B29: <CodeDescription xmlns=""> <Title>Solar
        concentration</Title> <Definition>Unit in which solar energy is
        converted to electricity using mirrors to concentrate the sun's
        energy to drive traditional steam turbines or
        engines.</Definition> </CodeDescription>
    :cvar B30: <CodeDescription xmlns=""> <Title>Wind
        unspecified</Title> <Definition>Unit in which wind energy is
        converted to electricity with equipment/devices not
        specified.</Definition> </CodeDescription>
    :cvar B31: <CodeDescription xmlns=""> <Title>Hydro-electric
        unspecified</Title> <Definition>Unit in which moving water
        energy is converted to electricity with equipment/devices not
        specified. </Definition> </CodeDescription>
    :cvar B32: <CodeDescription xmlns=""> <Title>Hydro-electric mixed
        pumped storage head installation</Title> <Definition>Unit in
        which moving water energy is converted to electricity using
        flowing water to generate electricity with a large dam and
        reservoirs. Mixed pumped storage plants use a combination of
        pumped storage and conventional hydroelectric plants with an
        upper reservoir that is replenished in part by natural inflows
        from a stream or river.</Definition> </CodeDescription>
    :cvar B33: <CodeDescription xmlns=""> <Title>Marine tidal</Title>
        <Definition>Unit in which marine energy from tides is converted
        to electricity.</Definition> </CodeDescription>
    :cvar B34: <CodeDescription xmlns=""> <Title>Marine wave</Title>
        <Definition>Unit in which marine energy from waves is converted
        to electricity.</Definition> </CodeDescription>
    :cvar B35: <CodeDescription xmlns=""> <Title>Marine currents</Title>
        <Definition>Unit in which marine energy from currents is
        converted to electricity.</Definition> </CodeDescription>
    :cvar B36: <CodeDescription xmlns=""> <Title>Marine pressure</Title>
        <Definition>Unit in which marine energy from pressure is
        converted to electricity.</Definition> </CodeDescription>
    :cvar B37: <CodeDescription xmlns=""> <Title>Thermal
        unspecified</Title> <Definition>Unit in which heat energy is
        converted to electricity with equipment/devices not specified in
        other thermal types.</Definition> </CodeDescription>
    :cvar B38: <CodeDescription xmlns=""> <Title>Thermal combined cycle
        gas turbine with heat recovery</Title> <Definition>Unit in which
        heat energy is converted to electricity called Combined Cycle
        Gas Turbine. The power is generated by the single or multiple
        gas turbine(s) in combination with the steam turbine(s). The
        unit might be equipped with waste heat recovery (e.g. to
        district heating network).</Definition> </CodeDescription>
    :cvar B39: <CodeDescription xmlns=""> <Title>Thermal steam turbine
        with back-pressure turbine (open cycle)</Title> <Definition>Unit
        in which heat energy is converted to electricity. The power is
        generated with the steam that is expanded in the back-pressure
        steam turbine with or without heat output (e.g. to district
        heating network).</Definition> </CodeDescription>
    :cvar B40: <CodeDescription xmlns=""> <Title>Thermal steam turbine
        with condensation turbine (closed cycle)</Title>
        <Definition>Unit in which heat energy is converted to
        electricity. The power is generated with the steam that is
        expanded in the condensation steam turbine with or without heat
        output (e.g. to district heating network).</Definition>
        </CodeDescription>
    :cvar B41: <CodeDescription xmlns=""> <Title>Thermal gas turbine
        with heat recovery</Title> <Definition>Unit in which heat energy
        is converted to electricity called Simple Cycle Gas Turbine. The
        power is generated by the gas turbine and the flue gas waste
        heat is recovered (e.g. to district heating
        network).</Definition> </CodeDescription>
    :cvar B42: <CodeDescription xmlns=""> <Title>Thermal internal
        combustion engine</Title> <Definition>An internal combustion
        engine is a heat engine in which the combustion of a fuel occurs
        with an oxidizer (usually air) in a combustion chamber that is
        an integral part of the working fluid flow circuit (e.g.
        reciprocating engine). The unit might be equipped with waste
        heat recovery (e.g. to district heating network).</Definition>
        </CodeDescription>
    :cvar B43: <CodeDescription xmlns=""> <Title>Thermal micro-
        turbine</Title> <Definition>Unit in which heat energy is
        converted to electricity called Simple Cycle Gas Turbine. The
        power is generated by the gas turbine (capacity less than
        500kWe). The unit might be equipped with waste heat recovery
        (e.g. to district heating network).</Definition>
        </CodeDescription>
    :cvar B44: <CodeDescription xmlns=""> <Title>Thermal Stirling
        engine</Title> <Definition>A Stirling engine is a heat engine
        that is operated by the cyclic compression and expansion of air
        or other gas (the working fluid) at different temperatures,
        resulting in a net conversion of heat energy to mechanical
        work.</Definition> </CodeDescription>
    :cvar B45: <CodeDescription xmlns=""> <Title>Thermal fuel
        cell</Title> <Definition>A fuel cell is an electrochemical cell
        that converts the chemical energy of a fuel (e.g. hydrogen) and
        an oxidizing agent (e.g. oxygen) into electricity through a pair
        of redox reactions.</Definition> </CodeDescription>
    :cvar B46: <CodeDescription xmlns=""> <Title>Thermal steam
        engine</Title> <Definition>A steam engine is a heat engine that
        performs mechanical work using steam as its working fluid. The
        steam engine uses the force produced by steam pressure to push a
        piston back and forth inside a cylinder.</Definition>
        </CodeDescription>
    :cvar B47: <CodeDescription xmlns=""> <Title>Thermal organic Rankine
        cycle</Title> <Definition>The Organic Rankine Cycle (ORC) is
        named for its use of an organic, high molecular mass fluid with
        a liquid-vapor phase change, or boiling point, occurring at a
        lower temperature than the water-steam phase change. The fluid
        allows Rankine cycle heat recovery from lower temperature
        sources such as biomass combustion, industrial waste heat,
        geothermal heat, solar ponds etc. The low-temperature heat is
        converted into useful work, that can itself be converted into
        electricity.</Definition> </CodeDescription>
    :cvar B48: <CodeDescription xmlns=""> <Title>Thermal gas turbine
        without heat recovery</Title> <Definition>Unit in which heat
        energy is converted to electricity called Simple Cycle Gas
        Turbine. The power is generated by the gas turbine and there is
        no flue gas waste heat recovery.</Definition> </CodeDescription>
    :cvar B49: <CodeDescription xmlns=""> <Title>Nuclear heavy water
        reactor</Title> <Definition>A unit in which the heat source is a
        pressurized heavy-water reactor (PHWR) that is a nuclear reactor
        that uses heavy water (deuterium oxide D2O) as its coolant and
        neutron moderator.</Definition> </CodeDescription>
    :cvar B50: <CodeDescription xmlns=""> <Title>Nuclear light water
        reactor</Title> <Definition>A unit in which the heat source is a
        light-water reactor (LWR) that is a type of thermal-neutron
        reactor that uses normal water, as both its coolant and neutron
        moderator � furthermore a solid form of fissile elements is used
        as fuel. </Definition> </CodeDescription>
    :cvar B51: <CodeDescription xmlns=""> <Title>Nuclear breeder</Title>
        <Definition>A unit in which the heat source is a nuclear reactor
        that generates more fissile material than it
        consumes.</Definition> </CodeDescription>
    :cvar B52: <CodeDescription xmlns=""> <Title>Nuclear graphite
        reactor</Title> <Definition>A unit in which the heat source is a
        graphite-moderated reactor that is a nuclear reactor that uses
        carbon as a neutron moderator, which allows natural uranium to
        be used as nuclear fuel.</Definition> </CodeDescription>
    :cvar B53: <CodeDescription xmlns=""> <Title>Temporary energy
        storage</Title> <Definition>A resource that is temporarily
        connected to the grid and that may store energy when connected,
        such as an electric vehicle.</Definition> </CodeDescription>
    :cvar B54: <CodeDescription xmlns=""> <Title>Permanent energy
        storage</Title> <Definition>A resource that is permanently
        connected to the grid and that may store energy when connected,
        such as a pumped hydro.</Definition> </CodeDescription>
    :cvar B55: <CodeDescription xmlns=""> <Title>Electric vehicle
        battery</Title> <Definition>A resource using electric vehicle
        batteries, commercial and private. The reason for separating
        vehicle batteries and non-vehicle batteries is that the vehicle
        batteries not necessarily is connected to the
        charger.</Definition> </CodeDescription>
    :cvar B56: <CodeDescription xmlns=""> <Title>Heat pump
        specified</Title> <Definition>A heat pump is a device that uses
        work to transfer heat from a cool space to a warm space by
        transferring thermal energy using a refrigeration
        cycle</Definition> </CodeDescription>
    :cvar B57: <CodeDescription xmlns=""> <Title>Heat pump
        electrical</Title> <Definition>A heat pump is a device that uses
        electricity to transfer heat from a cool space to a warm space
        by transferring thermal energy using a refrigeration
        cycle.</Definition> </CodeDescription>
    :cvar B58: <CodeDescription xmlns=""> <Title>Heat pump
        absorption</Title> <Definition>A heat pump is a device that uses
        absorption technology to transfer heat from a cool space to a
        warm space by transferring thermal energy using a refrigeration
        cycle.</Definition> </CodeDescription>
    :cvar B59: <CodeDescription xmlns=""> <Title>Auxiliary power
        unit</Title> <Definition>A technology that provides energy as a
        backup.</Definition> </CodeDescription>
    :cvar B60: <CodeDescription xmlns=""> <Title>Water electrolysis
        unspecified</Title> <Definition>Unspecified water electrolysis.
        </Definition> </CodeDescription>
    :cvar B61: <CodeDescription xmlns=""> <Title>Water electrolysis low
        temperature unspecified</Title> <Definition>Unspecified water
        electrolysis at low temperature as in an Alkaline or Proto-
        Exchange Membrane (PEM) fuel cell.</Definition>
        </CodeDescription>
    :cvar B62: <CodeDescription xmlns=""> <Title>Water electrolysis low
        temperature main product</Title> <Definition>Main product water
        electrolysis at low temperature as in an Alkaline or Proto-
        Exchange Membrane (PEM) fuel cell.</Definition>
        </CodeDescription>
    :cvar B63: <CodeDescription xmlns=""> <Title>Water electrolysis high
        temperature unspecified</Title> <Definition>Unspecified water
        electrolysis at high temperature as in a Solid Oxide
        Electrolysis Cell (SOEC) fuel cell.</Definition>
        </CodeDescription>
    :cvar B64: <CodeDescription xmlns=""> <Title>Steam methane reforming
        unspecified</Title> <Definition>Unspecified methane
        reforming.</Definition> </CodeDescription>
    :cvar B65: <CodeDescription xmlns=""> <Title>Steam methane reforming
        without CCS/CCU  unspecified</Title> <Definition>Main product
        methane reforming without Carbon Capture and Sequestration
        (CCS)/Carbon Capture and Use (CCU).  </Definition>
        </CodeDescription>
    :cvar B66: <CodeDescription xmlns=""> <Title>Steam methane reforming
        with CCS/CCU  unspecified</Title> <Definition>Unspecified
        methane reforming with Carbon Capture and Sequestration
        (CCS)/Carbon Capture and Use (CCU).    </Definition>
        </CodeDescription>
    :cvar B67: <CodeDescription xmlns=""> <Title>Steam methane reforming
        with CCS/CCU  main product</Title> <Definition>Main product
        methane reforming with Carbon Capture and Sequestration
        (CCS)/Carbon Capture and Use (CCU).    </Definition>
        </CodeDescription>
    :cvar B68: <CodeDescription xmlns=""> <Title>Partial oxidation
        unspecified</Title> <Definition>Unspecified partial
        oxidation.</Definition> </CodeDescription>
    :cvar B69: <CodeDescription xmlns=""> <Title>Autothermal reforming
        unspecified</Title> <Definition>Unspecified autothermal
        reforming.</Definition> </CodeDescription>
    :cvar B70: <CodeDescription xmlns=""> <Title>Methanol reforming
        unspecified</Title> <Definition>Unspecified methanol
        reforming.</Definition> </CodeDescription>
    :cvar B71: <CodeDescription xmlns=""> <Title>Ammonia reforming
        unspecified</Title> <Definition>Unspecified ammonia
        reforming.</Definition> </CodeDescription>
    :cvar B72: <CodeDescription xmlns=""> <Title>Ammonia
        gasification</Title> <Definition>Unspecified
        gasification.</Definition> </CodeDescription>
    :cvar B73: <CodeDescription xmlns=""> <Title>Chlor-alkali
        electrolysis unspecified</Title> <Definition>Unspecified alkali
        electrolysis.</Definition> </CodeDescription>
    :cvar B74: <CodeDescription xmlns=""> <Title>Chlor-alkali
        electrolysis by-product</Title> <Definition>Alkali electrolysis
        product.</Definition> </CodeDescription>
    :cvar B75: <CodeDescription xmlns=""> <Title>ACDC converter</Title>
        <Definition>ACDC converters are electrical circuits that
        transform alternating current (AC) into direct current (DC) and
        vice versa.</Definition> </CodeDescription>
    :cvar B76: <CodeDescription xmlns=""> <Title>Converter</Title>
        <Definition>Electrical device that converts current between AC
        and DC.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"
    A13 = "A13"
    A14 = "A14"
    B01 = "B01"
    B02 = "B02"
    B03 = "B03"
    B04 = "B04"
    B05 = "B05"
    B06 = "B06"
    B07 = "B07"
    B08 = "B08"
    B09 = "B09"
    B10 = "B10"
    B11 = "B11"
    B12 = "B12"
    B13 = "B13"
    B14 = "B14"
    B15 = "B15"
    B16 = "B16"
    B17 = "B17"
    B18 = "B18"
    B19 = "B19"
    B20 = "B20"
    B21 = "B21"
    B22 = "B22"
    B23 = "B23"
    B24 = "B24"
    B25 = "B25"
    B26 = "B26"
    B27 = "B27"
    B28 = "B28"
    B29 = "B29"
    B30 = "B30"
    B31 = "B31"
    B32 = "B32"
    B33 = "B33"
    B34 = "B34"
    B35 = "B35"
    B36 = "B36"
    B37 = "B37"
    B38 = "B38"
    B39 = "B39"
    B40 = "B40"
    B41 = "B41"
    B42 = "B42"
    B43 = "B43"
    B44 = "B44"
    B45 = "B45"
    B46 = "B46"
    B47 = "B47"
    B48 = "B48"
    B49 = "B49"
    B50 = "B50"
    B51 = "B51"
    B52 = "B52"
    B53 = "B53"
    B54 = "B54"
    B55 = "B55"
    B56 = "B56"
    B57 = "B57"
    B58 = "B58"
    B59 = "B59"
    B60 = "B60"
    B61 = "B61"
    B62 = "B62"
    B63 = "B63"
    B64 = "B64"
    B65 = "B65"
    B66 = "B66"
    B67 = "B67"
    B68 = "B68"
    B69 = "B69"
    B70 = "B70"
    B71 = "B71"
    B72 = "B72"
    B73 = "B73"
    B74 = "B74"
    B75 = "B75"
    B76 = "B76"


class AuctionTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Implicit</Title>
        <Definition>The auction is an implicit auction.</Definition>
        </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Explicit</Title>
        <Definition>The auction is an explicit auction.</Definition>
        </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Rule Based</Title>
        <Definition>The auction is a rule based auction.</Definition>
        </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Mixed</Title>
        <Definition>The auction is partially implicit and partially
        explicit.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Explicit/split</Title>
        <Definition>The auction concerns two explicit auctions on a
        split border.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Shadow auction</Title>
        <Definition>An explicit auction carried out in the case of the
        failure of an implicit auction.</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Flow-based</Title>
        <Definition>The allocation is an implicit auction using flow-
        based capacity calculation.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Continuous</Title>
        <Definition>The auction type is continuous, i.e. there is no
        gate closure time when bids from the market participants are
        collected. Instead allocation procedure takes place
        immediately.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"


class BusinessTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Production</Title>
        <Definition>The nature of the business being described is
        production details.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Internal trade</Title>
        <Definition>The nature of the business being described is
        internal trade details.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>External trade explicit
        capacity</Title> <Definition>The nature of the business being
        described is external trade details between two areas with
        limited capacity requiring a capacity agreement
        identification.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Consumption</Title>
        <Definition>The nature of the business being described is
        consumption details.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>External trade
        total</Title> <Definition>The nature of the business being
        described is external trade total.</Definition>
        </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>External trade without
        explicit capacity</Title> <Definition>The nature of the business
        being described is external trade details between two areas
        without requiring capacity allocation information.</Definition>
        </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Net Production /
        Consumption</Title> <Definition>Net production/consumption -
        where signed values will be used. With the following rules: In
        area=Out area, In party=Out party, + means production and -
        means consumption.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Net internal
        trade</Title> <Definition>Net internal trade - where the
        direction from out party (seller) to in party (buyer) is
        positive and the opposite direction is negative (with minus
        signs).</Definition> </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>IPP (Independent Power
        Producer)</Title> <Definition>A time series concerning the
        production schedule from an IPP.</Definition> </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Tertiary control
        </Title> <Definition>A time series concerning tertiary
        reserve.</Definition> </CodeDescription>
    :cvar A11: <CodeDescription xmlns=""> <Title>Primary control</Title>
        <Definition>A time series concerning primary
        reserve.</Definition> </CodeDescription>
    :cvar A12: <CodeDescription xmlns=""> <Title>Secondary
        control</Title> <Definition>A time series concerning secondary
        reserve.</Definition> </CodeDescription>
    :cvar A13: <CodeDescription xmlns=""> <Title>Load profile</Title>
        <Definition>A time series concerning a load profile as
        calculated by a metered data aggregator.</Definition>
        </CodeDescription>
    :cvar A14: <CodeDescription xmlns=""> <Title>Aggregated energy
        data</Title> <Definition>A time series concerning adjusted
        metered readings received from a metered data collector and
        aggregated and validated by a metered data
        aggregator.</Definition> </CodeDescription>
    :cvar A15: <CodeDescription xmlns=""> <Title>Losses</Title>
        <Definition>A time series concerning losses that have been
        calculated for a tieline or an area.</Definition>
        </CodeDescription>
    :cvar A16: <CodeDescription xmlns=""> <Title>Transits (CBT)</Title>
        <Definition>A time series concerning inter area transit flows
        determined for CBT requirements.</Definition> </CodeDescription>
    :cvar A17: <CodeDescription xmlns=""> <Title>Settlement
        deviation</Title> <Definition>A time series concerning the
        imbalance energy calculated by an imbalance settlement
        responsible.</Definition> </CodeDescription>
    :cvar A18: <CodeDescription xmlns=""> <Title>Technical constraint
        deviation</Title> <Definition>A time series defining the
        imbalance between schedules accepted by the system operator due
        to technical constraints and schedules declared by the balance
        responsible party.</Definition> </CodeDescription>
    :cvar A19: <CodeDescription xmlns=""> <Title>Balance energy
        deviation</Title> <Definition>A time series defining the
        imbalance between the schedule of a balance responsible party
        that has been corrected by the system operator after using
        balance energy bids and the schedule that was accepted by the
        system operator due to technical constraints.</Definition>
        </CodeDescription>
    :cvar A20: <CodeDescription xmlns=""> <Title>Imbalance
        volume</Title> <Definition>A time series defining the imbalance
        between the actual meter readings and the schedule of the
        balance responsible party corrected by the system operator after
        using balance energy bids.</Definition> </CodeDescription>
    :cvar A21: <CodeDescription xmlns=""> <Title>Unintended
        energy</Title> <Definition>A timeseries concerning the volume of
        an unintended cross-border exchange of energy.</Definition>
        </CodeDescription>
    :cvar A22: <CodeDescription xmlns=""> <Title>Frequency
        control</Title> <Definition>A time series concerning primary and
        secondary reserve.</Definition> </CodeDescription>
    :cvar A23: <CodeDescription xmlns=""> <Title>Balance
        management</Title> <Definition>A time series concerning energy
        balancing services.</Definition> </CodeDescription>
    :cvar A24: <CodeDescription xmlns=""> <Title>Total trade</Title>
        <Definition>A time series concerning the total of both the
        internal and external trades.</Definition> </CodeDescription>
    :cvar A25: <CodeDescription xmlns=""> <Title>General Capacity
        Information</Title> <Definition>A time series providing the
        total capacity available on a TSO border.</Definition>
        </CodeDescription>
    :cvar A26: <CodeDescription xmlns=""> <Title>Available transfer
        capacity (ATC)</Title> <Definition>Available transfer capacity
        for cross-border exchanges.</Definition> </CodeDescription>
    :cvar A27: <CodeDescription xmlns=""> <Title>Net transfer capacity
        (NTC)</Title> <Definition>Net transfer capacity for cross-border
        exchanges.</Definition> </CodeDescription>
    :cvar A28: <CodeDescription xmlns=""> <Title>Control Area
        Program</Title> <Definition>A time series providing the total
        exchanges between two TSOs (including the commercial
        transactions, the compensation program and the losses
        compensation program). Note this definition might change when
        UCTE brings forward its coding requirements.</Definition>
        </CodeDescription>
    :cvar A29: <CodeDescription xmlns=""> <Title>Already allocated
        capacity (AAC)</Title> <Definition>The already allocated
        capacity is the total amount of allocated transmission
        rights.</Definition> </CodeDescription>
    :cvar A30: <CodeDescription xmlns=""> <Title>Internal inter area
        trade</Title> <Definition>A trade that occurs between internal
        areas within a market balance area.</Definition>
        </CodeDescription>
    :cvar A31: <CodeDescription xmlns=""> <Title>Offered
        Capacity</Title> <Definition>The time series provides the
        offered capacity.</Definition> </CodeDescription>
    :cvar A32: <CodeDescription xmlns=""> <Title>Capacity transfer
        notification</Title> <Definition>The time series provides
        information concerning the notification of the transfer of
        capacity to another market participant.</Definition>
        </CodeDescription>
    :cvar A33: <CodeDescription xmlns=""> <Title>Authorised AAC</Title>
        <Definition>The time series in question provides the amount of
        transmission capacity rights to be nominated.</Definition>
        </CodeDescription>
    :cvar A34: <CodeDescription xmlns=""> <Title>Capacity rights</Title>
        <Definition>The time series in question provides the capacity
        rights allocated for a given border.</Definition>
        </CodeDescription>
    :cvar A35: <CodeDescription xmlns=""> <Title>Minimum authorised
        AAC</Title> <Definition>The time series in question provides the
        minimum amount of transmission capacity rights to be
        nominated.</Definition> </CodeDescription>
    :cvar A36: <CodeDescription xmlns=""> <Title>Maximum authorised
        AAC</Title> <Definition>The time series in question provides the
        maximum amount of transmission capacity rights to be
        nominated.</Definition> </CodeDescription>
    :cvar A37: <CodeDescription xmlns=""> <Title>Installed
        generation</Title> <Definition>The time series in question
        provides the installed generation.</Definition>
        </CodeDescription>
    :cvar A38: <CodeDescription xmlns=""> <Title>Available
        generation</Title> <Definition>The time series in question
        provides the available generation.</Definition>
        </CodeDescription>
    :cvar A40: <CodeDescription xmlns=""> <Title>Interconnection Trade
        Responsible Designation</Title> <Definition>The Time series in
        question provides the designation of the ITR that may nominate
        the capacity in question.</Definition> </CodeDescription>
    :cvar A41: <CodeDescription xmlns=""> <Title>Released AAC</Title>
        <Definition>The already allocated capacity (AAC) that has been
        released for resale.</Definition> </CodeDescription>
    :cvar A42: <CodeDescription xmlns=""> <Title>Requested capacity
        (with price)</Title> <Definition>The time series in question
        provides information concerning the requested capacity including
        price information.</Definition> </CodeDescription>
    :cvar A43: <CodeDescription xmlns=""> <Title>Requested capacity
        (without price)</Title> <Definition>The time series in question
        provides information concerning the requested capacity but
        excludes price information.</Definition> </CodeDescription>
    :cvar A44: <CodeDescription xmlns=""> <Title>Compensation
        program</Title> <Definition>Compensation of unintentional
        deviation is performed by exporting to / importing from the
        interconnected system during the compensation period by means of
        schedules as calculated during the accounting of unintentional
        deviations.</Definition> </CodeDescription>
    :cvar A45: <CodeDescription xmlns=""> <Title>Schedule activated
        reserves</Title> <Definition>The cross border or internal
        reserves that are to be activated through schedule
        nomination.</Definition> </CodeDescription>
    :cvar A46: <CodeDescription xmlns=""> <Title>System Operator
        redispatching</Title> <Definition>The cross border redispatching
        between System Operators that are to be activated through
        schedule nomination.</Definition> </CodeDescription>
    :cvar A47: <CodeDescription xmlns=""> <Title>Market capacity
        price</Title> <Definition>The price of the capacity offered on a
        given market.</Definition> </CodeDescription>
    :cvar A48: <CodeDescription xmlns=""> <Title>Market capacity price
        differential</Title> <Definition>The difference between the
        price of capacity in a Market Balance Area receiving the
        capacity (In Area) and the price of capacity in a Market Balance
        Area providing the capacity (Out Area), i.e. In Area Price - Out
        Area price.</Definition> </CodeDescription>
    :cvar A49: <CodeDescription xmlns=""> <Title>Inflow</Title>
        <Definition>The volume of water that flows into a reservoir in a
        given interval.</Definition> </CodeDescription>
    :cvar A50: <CodeDescription xmlns=""> <Title>Water
        extraction</Title> <Definition>The volume of water that can be
        extracted from a reservoir in a given interval.</Definition>
        </CodeDescription>
    :cvar A51: <CodeDescription xmlns=""> <Title>Turbined water</Title>
        <Definition>The volume of water that can be turbined in a plant
        in a given interval.</Definition> </CodeDescription>
    :cvar A52: <CodeDescription xmlns=""> <Title>Water spillage</Title>
        <Definition>The volume of water that is not turbined going
        through the spillway in a given interval.</Definition>
        </CodeDescription>
    :cvar A53: <CodeDescription xmlns=""> <Title>Planned
        maintenance</Title> <Definition>Maintenance has been planned for
        the object in question with a forecast ending date.</Definition>
        </CodeDescription>
    :cvar A54: <CodeDescription xmlns=""> <Title>Unplanned
        outage</Title> <Definition>An unplanned outage has occurred on
        the object in question.</Definition> </CodeDescription>
    :cvar A55: <CodeDescription xmlns=""> <Title>Use it Or Sell it
        (UIOSI) pricing</Title> <Definition>The time series provides
        information on the capacity resold in the "use it or sell it"
        process and its corresponding price.</Definition>
        </CodeDescription>
    :cvar A56: <CodeDescription xmlns=""> <Title>Compensation for
        auction cancellation where capacity is for resale</Title>
        <Definition>The time series provides information on the
        compensation of the capacity for resale following an auction
        cancellation.</Definition> </CodeDescription>
    :cvar A57: <CodeDescription xmlns=""> <Title>Resale pricing</Title>
        <Definition>For each Physical Transmission Rights holder, this
        document contains the resold capacity and its corresponding
        price.</Definition> </CodeDescription>
    :cvar A58: <CodeDescription xmlns=""> <Title>Curtailed capacity
        compensation</Title> <Definition>The time series provides
        information to compensate a party when curtailment is applied on
        the capacity obtained in a previous auction, resale or
        transfer.</Definition> </CodeDescription>
    :cvar A59: <CodeDescription xmlns=""> <Title>Use it Or Sell it
        (UIOSI) compensation</Title> <Definition>The time series
        provides information on the compensation for the capacity
        following an auction cancellation.</Definition>
        </CodeDescription>
    :cvar A60: <CodeDescription xmlns=""> <Title>Minimum
        possible</Title> <Definition>The time series provides a schedule
        of minimum possible values for a Resource Object. The nature of
        the flow could be defined by the attribute
        Direction.</Definition> </CodeDescription>
    :cvar A61: <CodeDescription xmlns=""> <Title>Maximum
        available</Title> <Definition>The time series provides a
        schedule of maximum available values for a Resource Object. The
        nature of the flow could be defined by the attribute
        Direction.</Definition> </CodeDescription>
    :cvar A62: <CodeDescription xmlns=""> <Title>Spot price</Title>
        <Definition>The time series provides the market spot prices from
        an auction.</Definition> </CodeDescription>
    :cvar A63: <CodeDescription xmlns=""> <Title>Minimum ATC</Title>
        <Definition>The Available Transmission Capacity that must be
        guaranteed because of regulatory constraints.</Definition>
        </CodeDescription>
    :cvar A64: <CodeDescription xmlns=""> <Title>Meter Measurement data
        </Title> <Definition>The data as provided for a meter
        measurement source.</Definition> </CodeDescription>
    :cvar A65: <CodeDescription xmlns=""> <Title>Accounting Point
        Relevant data </Title> <Definition>The metered data that is to
        be considered relevant for accounting purposes.</Definition>
        </CodeDescription>
    :cvar A66: <CodeDescription xmlns=""> <Title>Energy flow</Title>
        <Definition>Energy flow information.</Definition>
        </CodeDescription>
    :cvar A67: <CodeDescription xmlns=""> <Title>Power plant energy
        Schedule</Title> <Definition>Energy flow scheduled for a power
        plant.</Definition> </CodeDescription>
    :cvar A68: <CodeDescription xmlns=""> <Title>Compensation
        Requirements for the compensation period</Title> <Definition>The
        time series provides the compensation requirements for a given
        compensation period.</Definition> </CodeDescription>
    :cvar A69: <CodeDescription xmlns=""> <Title>Market coupling
        results</Title> <Definition>The time series provides the results
        of a market coupling auction.</Definition> </CodeDescription>
    :cvar A70: <CodeDescription xmlns=""> <Title>Production,
        unavailable</Title> <Definition>Production capacity that
        normally would be available, but due to maintenance or similar
        is temporarily unavailable.</Definition> </CodeDescription>
    :cvar A71: <CodeDescription xmlns=""> <Title>Supplementary available
        generation</Title> <Definition>The supplementary generation that
        is available.</Definition> </CodeDescription>
    :cvar A72: <CodeDescription xmlns=""> <Title>Interruptible
        consumption</Title> <Definition>The consumption that may be
        interrupted on request.</Definition> </CodeDescription>
    :cvar A73: <CodeDescription xmlns=""> <Title>Summarised Market
        Balance Area Schedule</Title> <Definition>A time series
        providing the total exchanges based on commercial transactions
        between two Market Balance Areas.</Definition>
        </CodeDescription>
    :cvar A74: <CodeDescription xmlns=""> <Title>Load Frequency Control
        Program Schedule</Title> <Definition>A time series providing the
        schedule information for the Load Frequency Control
        Program.</Definition> </CodeDescription>
    :cvar A75: <CodeDescription xmlns=""> <Title>Timeframe Independent
        Schedule</Title> <Definition>A time series providing the total
        exchanges of Timeframe Independent Schedules between two System
        Operators.</Definition> </CodeDescription>
    :cvar A76: <CodeDescription xmlns=""> <Title>Consumption
        curtailment</Title> <Definition>A time series providing the
        amount of voluntary consumption curtailed by the energy supplier
        of an end-consumer.</Definition> </CodeDescription>
    :cvar A77: <CodeDescription xmlns=""> <Title>Production,
        dispatchable</Title> <Definition>The nature of the business
        being described is dispatchable production details, i.e.
        generation output that can be changed by a request (activation
        order) of the TSO according with the applicable Market Rules.
        </Definition> </CodeDescription>
    :cvar A78: <CodeDescription xmlns=""> <Title>Consumption,
        dispatchable</Title> <Definition>The nature of the business
        being described is dispatchable consumption details, i.e.
        consumption output that can be changed by a request (activation
        order) of the TSO according with the applicable Market Rules.
        </Definition> </CodeDescription>
    :cvar A79: <CodeDescription xmlns=""> <Title>Production, non-
        dispatchable</Title> <Definition>The nature of the business
        being described is non-dispatchable production details, i.e.
        generation output that cannot be modified by an activation
        order.</Definition> </CodeDescription>
    :cvar A80: <CodeDescription xmlns=""> <Title>Consumption, non-
        dispatchable</Title> <Definition>The nature of the business
        being described is non-dispatchable consumption details, i.e.
        consumption output that cannot be modified by an activation
        order.</Definition> </CodeDescription>
    :cvar A81: <CodeDescription xmlns=""> <Title>Total Transfer Capacity
        (TTC)</Title> <Definition>The Total Transfer Capacity is the
        maximum exchange program between two areas compatible with
        operational security standards applicable at each system if
        future network conditions, generation and load patterns were
        perfectly known in advance.</Definition> </CodeDescription>
    :cvar A82: <CodeDescription xmlns=""> <Title>Mutual Emergency
        Assistance Service (MEAS) </Title> <Definition>The cross border
        Mutual Emergency Assistance Service between System Operators
        that are to be activated through schedule
        nomination.</Definition> </CodeDescription>
    :cvar A83: <CodeDescription xmlns=""> <Title>Auction cancelation
        </Title> <Definition>The time series covers auction cancellation
        right.</Definition> </CodeDescription>
    :cvar A84: <CodeDescription xmlns=""> <Title>Nomination
        curtailment</Title> <Definition>The time series covers
        nomination curtailment rights </Definition> </CodeDescription>
    :cvar A85: <CodeDescription xmlns=""> <Title>Internal
        redispatch</Title> <Definition>Redispatch to relieve Market
        Balance Area internal congestion.</Definition>
        </CodeDescription>
    :cvar A86: <CodeDescription xmlns=""> <Title>Control area balance
        energy</Title> <Definition>A sum of secondary, tertiary control
        as well as other energy that was used to balance a control
        area.</Definition> </CodeDescription>
    :cvar A87: <CodeDescription xmlns=""> <Title>Balancing energy
        price</Title> <Definition>Price of energy used to
        balance.</Definition> </CodeDescription>
    :cvar A88: <CodeDescription xmlns=""> <Title>Economised secondary
        reserve</Title> <Definition>The activated secondary reserve that
        had been economised due to pooled reserve
        management.</Definition> </CodeDescription>
    :cvar A89: <CodeDescription xmlns=""> <Title>Spinning
        reserve</Title> <Definition>The extra generating capacity that
        is available by increasing the production of generators that are
        already connected to the power system.</Definition>
        </CodeDescription>
    :cvar A90: <CodeDescription xmlns=""> <Title>Solar</Title>
        <Definition>The business being described concerns solar
        power.</Definition> </CodeDescription>
    :cvar A91: <CodeDescription xmlns=""> <Title>positive forecast
        margin</Title> <Definition>The business being described concerns
        a positive forecast margin.</Definition> </CodeDescription>
    :cvar A92: <CodeDescription xmlns=""> <Title>Negative forecast
        margin</Title> <Definition>The business being described concerns
        a negative forecast margin.</Definition> </CodeDescription>
    :cvar A93: <CodeDescription xmlns=""> <Title>Wind generation</Title>
        <Definition>The business being described concerns wind
        generation.</Definition> </CodeDescription>
    :cvar A94: <CodeDescription xmlns=""> <Title>Solar
        generation</Title> <Definition>The business being described
        concerns solar generation.</Definition> </CodeDescription>
    :cvar A95: <CodeDescription xmlns=""> <Title>Frequency containment
        reserve</Title> <Definition>The business being described
        concerns frequency containment reserve.</Definition>
        </CodeDescription>
    :cvar A96: <CodeDescription xmlns=""> <Title>Automatic frequency
        restoration reserve</Title> <Definition>The business being
        described concerns automatic frequency restoration
        reserve.</Definition> </CodeDescription>
    :cvar A97: <CodeDescription xmlns=""> <Title>Manual frequency
        restoration reserve</Title> <Definition>The business being
        described concerns manual frequency restoration
        reserve.</Definition> </CodeDescription>
    :cvar A98: <CodeDescription xmlns=""> <Title>Replacement
        reserve</Title> <Definition>The business being described
        concerns replacement reserve.</Definition> </CodeDescription>
    :cvar A99: <CodeDescription xmlns=""> <Title>Financial
        information</Title> <Definition>The business being described
        concerns financial information.</Definition> </CodeDescription>
    :cvar B01: <CodeDescription xmlns=""> <Title>Interconnector network
        evolution</Title> <Definition>The business being described
        concerns interconnector network evolution.</Definition>
        </CodeDescription>
    :cvar B02: <CodeDescription xmlns=""> <Title>Interconnector network
        dismantling</Title> <Definition>The business being described
        concerns interconnector network dismantling.</Definition>
        </CodeDescription>
    :cvar B03: <CodeDescription xmlns=""> <Title>Counter trade</Title>
        <Definition>The business being described concerns counter
        trades.</Definition> </CodeDescription>
    :cvar B04: <CodeDescription xmlns=""> <Title>Congestion
        costs</Title> <Definition>The business being described concerns
        congestion costs.</Definition> </CodeDescription>
    :cvar B05: <CodeDescription xmlns=""> <Title>Capacity allocated
        (including price)</Title> <Definition>The business being
        described concerns capacity allocation and includes price
        information.</Definition> </CodeDescription>
    :cvar B06: <CodeDescription xmlns=""> <Title>DC link
        constraint</Title> <Definition>The business being described
        concerns DC link constraints.</Definition> </CodeDescription>
    :cvar B07: <CodeDescription xmlns=""> <Title>Auction revenue</Title>
        <Definition>The business being described concerns auction
        revenue.</Definition> </CodeDescription>
    :cvar B08: <CodeDescription xmlns=""> <Title>Total nominated
        capacity</Title> <Definition>The business being described
        concerns the total nominated capacity.</Definition>
        </CodeDescription>
    :cvar B09: <CodeDescription xmlns=""> <Title>Net position</Title>
        <Definition>The business being described concerns net
        position.</Definition> </CodeDescription>
    :cvar B10: <CodeDescription xmlns=""> <Title>Congestion
        income</Title> <Definition>The business being described concerns
        congestion income.</Definition> </CodeDescription>
    :cvar B11: <CodeDescription xmlns=""> <Title>Production unit</Title>
        <Definition>The business being described concerns a production
        unit.</Definition> </CodeDescription>
    :cvar B12: <CodeDescription xmlns=""> <Title>Rounded market coupling
        results</Title> <Definition>Rounded outputs of the market
        coupling to be sent to TSOs and Market
        Participants.</Definition> </CodeDescription>
    :cvar B13: <CodeDescription xmlns=""> <Title>Allocation
        Revenue</Title> <Definition>The time series provides information
        on the revenue generated by the allocations.</Definition>
        </CodeDescription>
    :cvar B14: <CodeDescription xmlns=""> <Title>Production
        deviation</Title> <Definition>A time series concerning the
        imbalance energy between the metered production and the
        schedules calculated by an imbalance settlement
        responsible.</Definition> </CodeDescription>
    :cvar B15: <CodeDescription xmlns=""> <Title>Consumption
        deviation</Title> <Definition>A time series concerning the
        imbalance energy between  metered consumption and the forecasted
        consumption calculated by an imbalance settlement
        responsible.</Definition> </CodeDescription>
    :cvar B16: <CodeDescription xmlns=""> <Title>Transmission
        asset</Title> <Definition>The business being described concerns
        a transmission asset.</Definition> </CodeDescription>
    :cvar B17: <CodeDescription xmlns=""> <Title>Consumption
        unit</Title> <Definition>The business being described concerns a
        consumption unit.</Definition> </CodeDescription>
    :cvar B18: <CodeDescription xmlns=""> <Title>In-feed ATC</Title>
        <Definition>Available Transfer Capacity at the in-feed side of a
        DC tieline.</Definition> </CodeDescription>
    :cvar B19: <CodeDescription xmlns=""> <Title>Out-feed ATC</Title>
        <Definition>Available Transfer Capacity at the out-feed side of
        a DC tieline.</Definition> </CodeDescription>
    :cvar B20: <CodeDescription xmlns=""> <Title>Balance up regulation
        price</Title> <Definition>A time series concerning balance
        regulation market prices for up regulation.</Definition>
        </CodeDescription>
    :cvar B21: <CodeDescription xmlns=""> <Title>Balance down regulation
        price</Title> <Definition>A time series concerning balance
        regulation market prices for down regulation.</Definition>
        </CodeDescription>
    :cvar B22: <CodeDescription xmlns=""> <Title>Main direction</Title>
        <Definition>A time series concerning the direction of balance
        regulations.</Definition> </CodeDescription>
    :cvar B23: <CodeDescription xmlns=""> <Title>Consumption imbalance
        price</Title> <Definition>A time series concerning imbalance
        prices for consumption.</Definition> </CodeDescription>
    :cvar B24: <CodeDescription xmlns=""> <Title>Production sales
        imbalance price</Title> <Definition>A time series concerning
        imbalance prices for production sales.</Definition>
        </CodeDescription>
    :cvar B25: <CodeDescription xmlns=""> <Title>Production purchase
        imbalance price</Title> <Definition>A time series concerning
        imbalance prices for production purchase.</Definition>
        </CodeDescription>
    :cvar B26: <CodeDescription xmlns=""> <Title>Average balance price
        between MBAs</Title> <Definition>A time series concerning the
        average prices between Market Balance Areas.</Definition>
        </CodeDescription>
    :cvar B27: <CodeDescription xmlns=""> <Title>Pumped</Title>
        <Definition>A time series concerning the electricity consumption
        related to pumping.</Definition> </CodeDescription>
    :cvar B28: <CodeDescription xmlns=""> <Title>Large installation
        consumption</Title> <Definition>A time series concerning
        consumption from large installation.</Definition>
        </CodeDescription>
    :cvar B29: <CodeDescription xmlns=""> <Title>Metering Grid Area
        (MGA) imbalance</Title> <Definition>A time series concerning
        imbalance between reported consumption, production and exchange
        in a Metering Grid Area.</Definition> </CodeDescription>
    :cvar B30: <CodeDescription xmlns=""> <Title>HVDC Link
        settings</Title> <Definition>The time series in question
        provides HVDC Link settings.</Definition> </CodeDescription>
    :cvar B31: <CodeDescription xmlns=""> <Title>Transmission
        Reliability Margin (TRM)</Title> <Definition>A time series
        concerning Transmission Reliability Margin (TRM).</Definition>
        </CodeDescription>
    :cvar B32: <CodeDescription xmlns=""> <Title>Imbalance component for
        a pool</Title> <Definition>This information is used to provide
        to a pool manager the combined imbalance of all the pool
        participants.</Definition> </CodeDescription>
    :cvar B33: <CodeDescription xmlns=""> <Title>Area Control error
        (ACE)</Title> <Definition>The sum of the instantaneous
        difference between the actual and the set-point value of the
        measured total power value and Control Program including Virtual
        Tie-Lines for the power interchange of a LFC Area or a LFC Block
        and the frequency bias given by the product of the K-Factor of
        the LFC Area or the LFC Block and the Frequency
        Deviation.</Definition> </CodeDescription>
    :cvar B34: <CodeDescription xmlns=""> <Title>Area Control Error
        after Imbalance Netting</Title> <Definition>A time series
        concerning the Area Control Error after applying the  imbalance
        netting energy correction.</Definition> </CodeDescription>
    :cvar B35: <CodeDescription xmlns=""> <Title>Implicit and explicit
        trade total</Title> <Definition>The sum of cross border
        schedules based on implicit and explicit trades including long
        term, yearly, monthly, weekly, daily processes. </Definition>
        </CodeDescription>
    :cvar B36: <CodeDescription xmlns=""> <Title>Production units own
        consumption</Title> <Definition>The consumption of one or more
        production units.</Definition> </CodeDescription>
    :cvar B37: <CodeDescription xmlns=""> <Title>Constraint
        situation</Title> <Definition>The timeseries describes the
        constraint situation for a given TimeInterval. A constraint
        situation can be: - composed of a list of network elements in
        outage associated for each outage to a list of network elements
        on which remedial actions have been carried out accordingly to
        contingency process - or it can be an external
        constraint.</Definition> </CodeDescription>
    :cvar B38: <CodeDescription xmlns=""> <Title>Initial domain</Title>
        <Definition>The timeseries describe the full flow based domain
        for a given TimeInterval. Critical network elements are
        displayed in details and their impact on the market is
        quantified.</Definition> </CodeDescription>
    :cvar B39: <CodeDescription xmlns=""> <Title>Flow based domain
        adjusted to long term schedules</Title> <Definition>The
        timeseries describe the full flow based domain for a given
        TimeInterval adjusted to the latest update of the schedules.
        Critical network elements are displayed in details and their
        impact on the market is quantified.</Definition>
        </CodeDescription>
    :cvar B40: <CodeDescription xmlns=""> <Title>Network element
        constraint</Title> <Definition>The timeSeries describes limiting
        elements which are overloaded.</Definition> </CodeDescription>
    :cvar B41: <CodeDescription xmlns=""> <Title>Calculation opposition
        (Red Flag)</Title> <Definition>The timeSeries describes a party
        who is opposed to the calculation result and imposes its
        transfer capacity value.</Definition> </CodeDescription>
    :cvar B42: <CodeDescription xmlns=""> <Title>Base case proportional
        shift key</Title> <Definition>The GSK or LSK are proportional to
        the base case generation or load.</Definition>
        </CodeDescription>
    :cvar B43: <CodeDescription xmlns=""> <Title>Proportional to
        participation factors shift key</Title> <Definition>The GSK or
        LSK are proportional to the participation factors.</Definition>
        </CodeDescription>
    :cvar B44: <CodeDescription xmlns=""> <Title>Proportional to the
        remaining capacity shift key</Title> <Definition>The GSK is
        proportional to the remaining available capacity.</Definition>
        </CodeDescription>
    :cvar B45: <CodeDescription xmlns=""> <Title>Merit order shift
        key</Title> <Definition>The GSK is proportional to a merit order
        list.</Definition> </CodeDescription>
    :cvar B46: <CodeDescription xmlns=""> <Title>Wind speed</Title>
        <Definition>The TimeSeries provides information on the wind
        speed.</Definition> </CodeDescription>
    :cvar B47: <CodeDescription xmlns=""> <Title>Wind direction</Title>
        <Definition>The TimeSeries provides information on the wind
        direction.</Definition> </CodeDescription>
    :cvar B48: <CodeDescription xmlns=""> <Title>Solar
        irradiance</Title> <Definition>The TimeSeries provides
        information on the power per unit area produced by the sun in
        the form of electromagnetic radiation.</Definition>
        </CodeDescription>
    :cvar B49: <CodeDescription xmlns=""> <Title>Air temperature</Title>
        <Definition>The TimeSeries provides information on the air
        temperature.</Definition> </CodeDescription>
    :cvar B50: <CodeDescription xmlns=""> <Title>Cloudiness</Title>
        <Definition>The TimeSeries provides information on the
        cloudiness, i.e. the level of coverage of the sky with
        clouds.</Definition> </CodeDescription>
    :cvar B51: <CodeDescription xmlns=""> <Title>Air humidity</Title>
        <Definition>The TimeSeries provides information on the level of
        humidity of the air.</Definition> </CodeDescription>
    :cvar B52: <CodeDescription xmlns=""> <Title>Atmospheric
        pressure</Title> <Definition>The TimeSeries provides information
        on the atmospheric pressure.</Definition> </CodeDescription>
    :cvar B53: <CodeDescription xmlns=""> <Title>Precipitation</Title>
        <Definition>The TimeSeries provides information on the amount of
        rain, snow, etc. that falls on the ground.</Definition>
        </CodeDescription>
    :cvar B54: <CodeDescription xmlns=""> <Title>Network constraint
        situation that constraints the market</Title> <Definition>The
        TimeSeries describes the network elements, that constraints the
        market, to be taken into account to simulate a network
        constraint during the network load flow studies. The network
        situation includes the contingencies, the remedial actions, the
        monitored network elements and the potential additional
        constraints.</Definition> </CodeDescription>
    :cvar B55: <CodeDescription xmlns=""> <Title>Contingency</Title>
        <Definition>The TimeSeries describes the network elements part
        of the contingency to be simulated for a given
        TimeInterval.</Definition> </CodeDescription>
    :cvar B56: <CodeDescription xmlns=""> <Title>Remedial Action</Title>
        <Definition>The TimeSeries describes a set of remedial actions
        for a given TimeInterval.</Definition> </CodeDescription>
    :cvar B57: <CodeDescription xmlns=""> <Title>Monitored Network
        Element</Title> <Definition>The TimeSeries describes the network
        elements to be monitored during the network load flow
        studies.</Definition> </CodeDescription>
    :cvar B58: <CodeDescription xmlns=""> <Title>Busbar</Title>
        <Definition>The TimeSeries describes the network elements that
        composed a busbar.</Definition> </CodeDescription>
    :cvar B59: <CodeDescription xmlns=""> <Title>Network Element</Title>
        <Definition>The TimeSeries describes network
        elements.</Definition> </CodeDescription>
    :cvar B60: <CodeDescription xmlns=""> <Title>SPS</Title>
        <Definition>The TimeSeries describes the network elements
        managed by a Special Protection System
        (automation).</Definition> </CodeDescription>
    :cvar B61: <CodeDescription xmlns=""> <Title>Aggregated netted
        external market schedule</Title> <Definition>The aggregated
        netted external market schedules for a given
        border.</Definition> </CodeDescription>
    :cvar B62: <CodeDescription xmlns=""> <Title>Aggregated netted
        external TSO schedule</Title> <Definition>The aggregated netted
        external TSO schedules for a given border.</Definition>
        </CodeDescription>
    :cvar B63: <CodeDescription xmlns=""> <Title>Aggregated netted
        external schedule</Title> <Definition>The aggregated netted
        external schedules for a given border.</Definition>
        </CodeDescription>
    :cvar B64: <CodeDescription xmlns=""> <Title>Netted area AC
        position</Title> <Definition>The AC position for a given
        area.</Definition> </CodeDescription>
    :cvar B65: <CodeDescription xmlns=""> <Title>Netted area
        position</Title> <Definition>The netted aggregation of all AC
        external schedules of an area plus the aggregated External
        Netted Schedules of related HVDC links of an area.</Definition>
        </CodeDescription>
    :cvar B66: <CodeDescription xmlns=""> <Title>Interconnection shift
        key</Title> <Definition>The shift key series describes the
        amount of power to be shifted from a border area. </Definition>
        </CodeDescription>
    :cvar B67: <CodeDescription xmlns=""> <Title>DC flow with
        losses</Title> <Definition>DC flow with losses refers to the
        values at the importing end of the DC line.</Definition>
        </CodeDescription>
    :cvar B68: <CodeDescription xmlns=""> <Title>DC flow without
        losses</Title> <Definition>DC flow without losses refers to the
        values at the exporting end of the DC line.</Definition>
        </CodeDescription>
    :cvar B69: <CodeDescription xmlns=""> <Title>minimum value of netted
        area position</Title> <Definition>That value which a netted area
        position must not fall below for a given area.</Definition>
        </CodeDescription>
    :cvar B70: <CodeDescription xmlns=""> <Title>maximum value of netted
        area position</Title> <Definition>That value which a netted area
        position must not exceed for a given optimisation area.
        </Definition> </CodeDescription>
    :cvar B71: <CodeDescription xmlns=""> <Title>maximum value of DC
        flow</Title> <Definition>That value which a balanced DC flow
        must not exceed for a given DC line on exporting end. When
        aligning DC flows CGMA algorithm will respect this
        constraint.</Definition> </CodeDescription>
    :cvar B72: <CodeDescription xmlns=""> <Title>minimum value of DC
        flow</Title> <Definition>That value which a balanced DC flow
        must not fall below for a given DC line on exporting end.
        Currently this business type is only included for consistency
        reasons. It is always set to 0. This constraint might, however,
        be used in future. When aligning DC flows the CGMA algorithm
        will respect this constraint.</Definition> </CodeDescription>
    :cvar B73: <CodeDescription xmlns=""> <Title>indicative AC
        flow</Title> <Definition>It is the hypothetical flow on the
        aggregate of all AC tie lines of an electrical border between
        two optimisation areas. It results from the adjustments to the
        preliminary netted area positions of all optimisation areas made
        by the CGMA algorithm. Indicative AC flows are an artefact of
        the CGMA algorithm, and do not correspond to physical
        flows</Definition> </CodeDescription>
    :cvar B74: <CodeDescription xmlns=""> <Title>Offer</Title>
        <Definition>The time series provides an offer to provide
        reserves. </Definition> </CodeDescription>
    :cvar B75: <CodeDescription xmlns=""> <Title>Need</Title>
        <Definition>The time series provides a requirement for reserves.
        </Definition> </CodeDescription>
    :cvar B76: <CodeDescription xmlns=""> <Title>Opportunity costs or
        benefits</Title> <Definition>The time series describes any
        opportunity costs or benefits.</Definition> </CodeDescription>
    :cvar B77: <CodeDescription xmlns=""> <Title>Financial compensation
        or penalties</Title> <Definition>The time series describes any
        financial compensation or penalties</Definition>
        </CodeDescription>
    :cvar B78: <CodeDescription xmlns=""> <Title>Global
        radiation</Title> <Definition>The total short-wave radiation
        from the Global radiation is the total short-wave radiation from
        the sky falling onto a horizontal surface on the ground. It
        includes both the direct solar radiation and the diffuse
        radiation resulting from reflected or scattered
        sunlight.</Definition> </CodeDescription>
    :cvar B79: <CodeDescription xmlns=""> <Title>Diffuse
        radiation</Title> <Definition>Radiation resulting from reflected
        or scattered sunlight.</Definition> </CodeDescription>
    :cvar B80: <CodeDescription xmlns=""> <Title>Direct solar
        radiation</Title> <Definition>Radiation resulting from direct
        sunlight</Definition> </CodeDescription>
    :cvar B81: <CodeDescription xmlns=""> <Title>Outage (OUT)</Title>
        <Definition>Outage process: Element is out of operation due to
        planned maintenance or due to an unplanned/forced outage. Outage
        may be used as a synonym for unavailability. </Definition>
        </CodeDescription>
    :cvar B82: <CodeDescription xmlns=""> <Title>Special switching state
        (SSS)</Title> <Definition>Outage Process: This state applies to
        grid elements which are in operation in an exceptional state
        (e.g. separated nodes operation).</Definition>
        </CodeDescription>
    :cvar B83: <CodeDescription xmlns=""> <Title>Testing (TEST)</Title>
        <Definition>Outage process: TESTING means any element status is
        possible - ON or OUT. This status applies either between first
        connection and final commissioning of the relevant asset, or
        directly following maintenance of the relevant
        asset.</Definition> </CodeDescription>
    :cvar B84: <CodeDescription xmlns=""> <Title>Auxiliary busbar
        operation</Title> <Definition>Outage process: Element is in
        operation but connected via auxiliary busbar</Definition>
        </CodeDescription>
    :cvar B85: <CodeDescription xmlns=""> <Title>Automatic
        reclosing</Title> <Definition>Outage process: Protection
        function Automatic reclosing is switched off for electric
        line</Definition> </CodeDescription>
    :cvar B86: <CodeDescription xmlns=""> <Title>Busbar
        protection</Title> <Definition>Protection function busbar
        protection is switched off</Definition> </CodeDescription>
    :cvar B87: <CodeDescription xmlns=""> <Title>Phase Shift
        Angle</Title> <Definition>The maximum phase shift angle allowed
        between two network elements. </Definition> </CodeDescription>
    :cvar B88: <CodeDescription xmlns=""> <Title>Base Case Network
        Situation</Title> <Definition>The TimeSeries describes the
        network elements to be taken into account to simulate a base
        case network situation during the network load flow studies,
        without any contingency.</Definition> </CodeDescription>
    :cvar B89: <CodeDescription xmlns=""> <Title>Inter-TSO
        assistance</Title> <Definition>Cross border assistance schedule
        between TSOs not interconnected directly. </Definition>
        </CodeDescription>
    :cvar B90: <CodeDescription xmlns=""> <Title>FlexibleNeed</Title>
        <Definition>The business type indicates that the need is
        optional.</Definition> </CodeDescription>
    :cvar B91: <CodeDescription xmlns=""> <Title>GLSK Limitation</Title>
        <Definition>A constraint related to a GLSK maximum or minimum
        limitation in the production or/and consumption
        shift.</Definition> </CodeDescription>
    :cvar B92: <CodeDescription xmlns=""> <Title>Capacity ramping
        limitation</Title> <Definition>A constraint related to a ramping
        limitation on the capacity offered at a given
        border.</Definition> </CodeDescription>
    :cvar B93: <CodeDescription xmlns=""> <Title>interconnector
        capacity</Title> <Definition>The maximum capacity that can be
        exchanged on an interconnector, excluding external factor on
        both ends. </Definition> </CodeDescription>
    :cvar B94: <CodeDescription xmlns=""> <Title>Must Run</Title>
        <Definition>A time series concerning must run
        generation.</Definition> </CodeDescription>
    :cvar B95: <CodeDescription xmlns=""> <Title>Procured
        capacity</Title> <Definition>An accepted offer of balancing
        capacity.</Definition> </CodeDescription>
    :cvar B96: <CodeDescription xmlns=""> <Title>Used capacity</Title>
        <Definition>The used cross-zonal balancing
        capacity.</Definition> </CodeDescription>
    :cvar B97: <CodeDescription xmlns=""> <Title>Estimated costs</Title>
        <Definition>Estimated costs of the process.</Definition>
        </CodeDescription>
    :cvar B98: <CodeDescription xmlns=""> <Title>Estimated
        benefits</Title> <Definition>Estimated benefits of the
        process.</Definition> </CodeDescription>
    :cvar B99: <CodeDescription xmlns=""> <Title>Load Shedding</Title>
        <Definition>A time series concerning a load shedding used to
        avoid failure of the power system.</Definition>
        </CodeDescription>
    :cvar C01: <CodeDescription xmlns=""> <Title>Remaining
        Capacity</Title> <Definition>A time series concerning the
        remaining capacity.</Definition> </CodeDescription>
    :cvar C02: <CodeDescription xmlns=""> <Title>Indicator of generation
        capacity adequacy</Title> <Definition>Indicator of adequacy, it
        indicates if there is final generation remaining capacity after
        SMTA calculation.</Definition> </CodeDescription>
    :cvar C03: <CodeDescription xmlns=""> <Title>Income from price
        divergence without congestions</Title> <Definition>The time
        series describes income due to price divergence without
        congestion between bidding zones.</Definition>
        </CodeDescription>
    :cvar C04: <CodeDescription xmlns=""> <Title>Push-button</Title>
        <Definition>The cross-border Push-button service between System
        Operators.</Definition> </CodeDescription>
    :cvar C05: <CodeDescription xmlns=""> <Title>Intertripping</Title>
        <Definition>The cross-border Intertripping service between
        System Operators.</Definition> </CodeDescription>
    :cvar C06: <CodeDescription xmlns=""> <Title>Emergency
        instruction</Title> <Definition>The cross-border Emergency
        instruction service between System Operators.</Definition>
        </CodeDescription>
    :cvar C07: <CodeDescription xmlns=""> <Title>Ramp management</Title>
        <Definition>The schedule resulting from cross-border Ramp
        management service between System Operators.</Definition>
        </CodeDescription>
    :cvar C08: <CodeDescription xmlns=""> <Title>Profile
        smoothing</Title> <Definition>The schedule resulting from cross-
        border Profile smoothing service between System
        Operators.</Definition> </CodeDescription>
    :cvar C09: <CodeDescription xmlns=""> <Title>Emergency reallocation
        deselection</Title> <Definition>The schedule resulting from
        cross-border Emergency reallocation deselection service between
        System Operators.</Definition> </CodeDescription>
    :cvar C10: <CodeDescription xmlns=""> <Title>SO-SO-trade</Title>
        <Definition>The generic cross border trade between System
        Operators.</Definition> </CodeDescription>
    :cvar C11: <CodeDescription xmlns=""> <Title>Production
        reduction</Title> <Definition>A time series providing the volume
        of production reduced by an energy provider / producer /
        supplier.</Definition> </CodeDescription>
    :cvar C12: <CodeDescription xmlns=""> <Title>Maximum power
        exchange</Title> <Definition>The timeseries provides the maximum
        admissible power flow between two bidding zones respecting
        operational security limits taking into account N-1
        criterion.</Definition> </CodeDescription>
    :cvar C13: <CodeDescription xmlns=""> <Title>Maximum power exchange
        after remedial actions</Title> <Definition>The timeseries
        provides the maximum admissible power flow between two bidding
        zones after remedial actions.</Definition> </CodeDescription>
    :cvar C14: <CodeDescription xmlns=""> <Title>Network constraint
        situation that cannot limit the market</Title> <Definition>The
        TimeSeries describes the network elements, that cannot limit the
        market, to be taken into account to simulate a network
        constraint during the network load flow studies. The network
        situation includes the contingencies, the remedial actions, the
        monitored network elements and the potential additional
        constraints.</Definition> </CodeDescription>
    :cvar C15: <CodeDescription xmlns=""> <Title>Flat participation for
        all generators or loads</Title> <Definition>Flat GSK factors of
        all generators or loads, independently of the size.</Definition>
        </CodeDescription>
    :cvar C16: <CodeDescription xmlns=""> <Title>Proportional to
        installed capacity of generators</Title> <Definition>Generators
        participate relative to their maximum (installed) capacity
        (MW).</Definition> </CodeDescription>
    :cvar C17: <CodeDescription xmlns=""> <Title>Market price and total
        volume</Title> <Definition>A time series concerning market price
        and total volume.</Definition> </CodeDescription>
    :cvar C18: <CodeDescription xmlns=""> <Title>Import price</Title>
        <Definition>A time series concerning import price (the volume-
        weighted price average of all accepted bids).</Definition>
        </CodeDescription>
    :cvar C19: <CodeDescription xmlns=""> <Title>Capacity allocated
        (excluding price)</Title> <Definition>The business being
        described concerns capacity allocation and excludes price
        information.</Definition> </CodeDescription>
    :cvar C20: <CodeDescription xmlns=""> <Title>Common Grid Model
        Equipment</Title> <Definition>The timeseries provides equipment
        related to the Common Grid Model (CGM).</Definition>
        </CodeDescription>
    :cvar C21: <CodeDescription xmlns=""> <Title>Exchanged balancing
        reserve capacity</Title> <Definition>The balancing reserve
        capacity exchanged between areas.</Definition>
        </CodeDescription>
    :cvar C22: <CodeDescription xmlns=""> <Title>Shared balancing
        reserve capacity</Title> <Definition>The balancing reserve
        capacity shared between areas.</Definition> </CodeDescription>
    :cvar C23: <CodeDescription xmlns=""> <Title>Share of reserve
        capacity</Title> <Definition>A time series concerning the share
        of reserve capacity.</Definition> </CodeDescription>
    :cvar C24: <CodeDescription xmlns=""> <Title>Actual reserve
        capacity</Title> <Definition>A timeseries concerning actual
        reserve capacity.</Definition> </CodeDescription>
    :cvar C25: <CodeDescription xmlns=""> <Title>K-factor</Title>
        <Definition>K-factor as stated in the SO GL Art. 2 (45). It is
        also known as Frequency Bias.</Definition> </CodeDescription>
    :cvar C26: <CodeDescription xmlns=""> <Title>Frequency Containment
        Reserve-Normal (FCR-N)</Title> <Definition>FCR-N is a reserve
        that is automatically activated in both directions around a set
        point when the frequency varies between 50.10 Hz and 49.90 Hz
        after an imbalance.</Definition> </CodeDescription>
    :cvar C27: <CodeDescription xmlns=""> <Title>Frequency Containment
        Reserve-Disturbance (FCR-D)</Title> <Definition>FCR-D is a
        reserve that is automatically activated when the frequency falls
        below 49.90 Hz or rises above 50.1 Hz after an
        imbalance.</Definition> </CodeDescription>
    :cvar C28: <CodeDescription xmlns=""> <Title>Internal trade
        difference</Title> <Definition>A time series concerning internal
        trade difference, within an area, such as a Bidding Zone or
        Scheduling Area. The internal trade difference is the difference
        between trades reported from an out party (seller) and an in
        party (buyer). </Definition> </CodeDescription>
    :cvar C29: <CodeDescription xmlns=""> <Title>Small scale
        production</Title> <Definition>Production from small scale
        production plants.</Definition> </CodeDescription>
    :cvar C30: <CodeDescription xmlns=""> <Title>System price</Title>
        <Definition>The system price is an unconstrained market clearing
        reference price. It is calculated without any congestion
        restrictions by setting capacities to infinity.</Definition>
        </CodeDescription>
    :cvar C31: <CodeDescription xmlns=""> <Title>Wind gust</Title>
        <Definition>An increase in the speed of the wind lasting for a
        short period.</Definition> </CodeDescription>
    :cvar C32: <CodeDescription xmlns=""> <Title>Area imbalance</Title>
        <Definition>A time series concerning imbalance between planned
        consumption, production and exchange in an Area.</Definition>
        </CodeDescription>
    :cvar C33: <CodeDescription xmlns=""> <Title>Unintended energy
        price</Title> <Definition>A timeseries concerning the price of
        the unintended cross-border exchange of energy.</Definition>
        </CodeDescription>
    :cvar C34: <CodeDescription xmlns=""> <Title>Frequency containment
        process energy</Title> <Definition>A timeseries containing the
        volume of energy resulting from the frequency containment
        process.</Definition> </CodeDescription>
    :cvar C35: <CodeDescription xmlns=""> <Title>Frequency containment
        process energy price</Title> <Definition>A timeseries containing
        the energy price from the frequency containment
        process.</Definition> </CodeDescription>
    :cvar C36: <CodeDescription xmlns=""> <Title>Ramping period
        energy</Title> <Definition>A timeseries containing the volume of
        energy exchanged as a result of ramping between different ANES
        values.</Definition> </CodeDescription>
    :cvar C37: <CodeDescription xmlns=""> <Title>Ramping period energy
        price</Title> <Definition>A timeseries containing the price of
        the energy exchanged as a result of ramping between different
        ANES values.</Definition> </CodeDescription>
    :cvar C38: <CodeDescription xmlns=""> <Title>Frequency
        deviation</Title> <Definition>A timeseries concerning the
        difference between the actual and the nominal frequency of a
        synchronous area.</Definition> </CodeDescription>
    :cvar C39: <CodeDescription xmlns=""> <Title>Day-Ahead market
        price</Title> <Definition>A timeseries concerning Day-Ahead
        market prices.</Definition> </CodeDescription>
    :cvar C40: <CodeDescription xmlns=""> <Title>Conditional bid</Title>
        <Definition>Standard product bid that is conditional on bids
        submitted outside of common platform.</Definition>
        </CodeDescription>
    :cvar C41: <CodeDescription xmlns=""> <Title>Thermal limit</Title>
        <Definition>The current causing a given network element to work
        outside of the range of safe operating
        temperatures.</Definition> </CodeDescription>
    :cvar C42: <CodeDescription xmlns=""> <Title>Frequency Limit</Title>
        <Definition>A constraint related to the containment of frequency
        deviations within a given area.</Definition> </CodeDescription>
    :cvar C43: <CodeDescription xmlns=""> <Title>Voltage limit</Title>
        <Definition>The maximum or minimum permissible voltage within
        normal operation state of a given network element.</Definition>
        </CodeDescription>
    :cvar C44: <CodeDescription xmlns=""> <Title>Current limit</Title>
        <Definition>The maximum permissible current within normal
        operation state of a given network element.</Definition>
        </CodeDescription>
    :cvar C45: <CodeDescription xmlns=""> <Title>Short circuit current
        limit</Title> <Definition>The maximum permissible short-circuit
        current within normal operation state of a given network
        element.</Definition> </CodeDescription>
    :cvar C46: <CodeDescription xmlns=""> <Title>Dynamic stability
        limit</Title> <Definition>A maximum permissible load ensuring
        the control of oscillations in the grid and avoiding the loss of
        synchronism.</Definition> </CodeDescription>
    :cvar C47: <CodeDescription xmlns=""> <Title>Disconnection</Title>
        <Definition>A timeseries describing disconnection of a TSO from
        a common platform.</Definition> </CodeDescription>
    :cvar C48: <CodeDescription xmlns=""> <Title>Intended energy with
        positive price</Title> <Definition>A timeseries concerning the
        amount of intended energy with prices higher than zero (and
        including zero).</Definition> </CodeDescription>
    :cvar C49: <CodeDescription xmlns=""> <Title>Intended energy with
        negative price</Title> <Definition>A timeseries concerning the
        amount of intended energy with prices lower than zero (excluding
        zero).</Definition> </CodeDescription>
    :cvar C50: <CodeDescription xmlns=""> <Title>Decopuling</Title>
        <Definition>A time series describing decoupling of an
        area.</Definition> </CodeDescription>
    :cvar C51: <CodeDescription xmlns=""> <Title>Resource capacity
        unit</Title> <Definition>A timeseries containing information
        about resource capacity units.</Definition> </CodeDescription>
    :cvar C52: <CodeDescription xmlns=""> <Title>Resource entry capacity
        data</Title> <Definition>A timeseries containing the resource
        capacity that can be allocated to an eligible resource capacity
        operator from another area.</Definition> </CodeDescription>
    :cvar C53: <CodeDescription xmlns=""> <Title>Resource capacity
        obligation data</Title> <Definition>A timeseries containing the
        resource capacity operator obligation to guarantee
        delivery.</Definition> </CodeDescription>
    :cvar C54: <CodeDescription xmlns=""> <Title>Available
        energy</Title> <Definition>A timeseries concerning the available
        energy.</Definition> </CodeDescription>
    :cvar C55: <CodeDescription xmlns=""> <Title>Production
        curtailment</Title> <Definition>A timeseries concerning the
        curtailment of production.</Definition> </CodeDescription>
    :cvar C56: <CodeDescription xmlns=""> <Title>Rounding error</Title>
        <Definition>A timeseries describing a rounding
        error.</Definition> </CodeDescription>
    :cvar C57: <CodeDescription xmlns=""> <Title>Metered
        frequency</Title> <Definition>The timeseries provides
        information about metered frequency.</Definition>
        </CodeDescription>
    :cvar C58: <CodeDescription xmlns=""> <Title>Adjusted TTC to the
        nominal criteria</Title> <Definition>The exchange program
        between two areas which guarantees that the Margin Available for
        Cross-Zonal Trade (MACZT) fulfils the nominal criteria at least
        on the most limiting Critical Network Element with Contingency
        (CNEC) which limits the transfer capacity.</Definition>
        </CodeDescription>
    :cvar C59: <CodeDescription xmlns=""> <Title>Adjusted TTC to the
        nominal criteria with TSOs limitation</Title> <Definition>The
        exchange program between two areas which allows the Margin
        Available for Cross-Zonal Trade (MACZT) on, at least, the most
        limiting Critical Network Element with Contingency (CNEC) to get
        closer to the nominal criteria fulfilment with a limited impact
        on the rest of the network.</Definition> </CodeDescription>
    :cvar C60: <CodeDescription xmlns=""> <Title>Frequency deviation
        larger than standard deviation</Title> <Definition>Total time in
        which the absolute value of the instantaneous frequency
        deviation was larger than the standard frequency
        deviation.</Definition> </CodeDescription>
    :cvar C61: <CodeDescription xmlns=""> <Title>Frequency deviation
        larger than maximum deviation</Title> <Definition>Total time in
        which the absolute value of the instantaneous frequency
        deviation was larger than the maximum instantaneous frequency
        deviation.</Definition> </CodeDescription>
    :cvar C62: <CodeDescription xmlns=""> <Title>Frequency deviation not
        returned to 50%</Title> <Definition>Number of events in which
        the absolute value of the instantaneous frequency deviation of
        the synchronous area exceeded 200 % of the standard frequency
        deviation as stated in SO GL (EU) regulation Art
        131.1.a.vi.</Definition> </CodeDescription>
    :cvar C63: <CodeDescription xmlns=""> <Title>Frequency deviation not
        returned to restoration range</Title> <Definition>Number of
        events in which the absolute value of the instantaneous
        frequency deviation of the synchronous area exceeded 200 % of
        the standard frequency deviation.</Definition>
        </CodeDescription>
    :cvar C64: <CodeDescription xmlns=""> <Title>Frequency deviation
        outside recovery range</Title> <Definition>Number of events for
        which the absolute value of the instantaneous frequency
        deviation was outside of the frequency recovery
        range.</Definition> </CodeDescription>
    :cvar C65: <CodeDescription xmlns=""> <Title>Frequency</Title>
        <Definition>A time series describing measurement
        frequency.</Definition> </CodeDescription>
    :cvar C66: <CodeDescription xmlns=""> <Title>Mean value</Title>
        <Definition>A time series describing mean values.</Definition>
        </CodeDescription>
    :cvar C67: <CodeDescription xmlns=""> <Title>Standard
        deviation</Title> <Definition>A time series describing standard
        deviation.</Definition> </CodeDescription>
    :cvar C68: <CodeDescription xmlns=""> <Title>Percentile</Title>
        <Definition>A time series describing percentiles.</Definition>
        </CodeDescription>
    :cvar C69: <CodeDescription xmlns=""> <Title>Measured frequency
        resolution</Title> <Definition>A time series describing the
        resolution of a measured frequency.</Definition>
        </CodeDescription>
    :cvar C70: <CodeDescription xmlns=""> <Title>Accuracy</Title>
        <Definition>A time series describing measurement
        accuracy.</Definition> </CodeDescription>
    :cvar C71: <CodeDescription xmlns=""> <Title>FRCE outside level 1
        range</Title> <Definition>The number of time intervals in which
        the average value of the FRCE was outside the Level 1 FRCE range
        as stated in SO GL. (EU) regulation Art 131.1.b.i.</Definition>
        </CodeDescription>
    :cvar C72: <CodeDescription xmlns=""> <Title>FRCE outside level 2
        range</Title> <Definition>The number of time intervals in which
        the average value of the FRCE was outside the Level 2 FRCE range
        as stated in SO GL (EU) regulation. Art 131.1.b.i.</Definition>
        </CodeDescription>
    :cvar C73: <CodeDescription xmlns=""> <Title>FRCE exceeded 60% of
        FRR capacity</Title> <Definition>The number of events for which
        the FRCE exceeded 60 % of the reserve capacity on FRR as stated
        in SO GL (EU) regulation Art 131.1.b.ii.</Definition>
        </CodeDescription>
    :cvar C74: <CodeDescription xmlns=""> <Title>FRCE exceeded steady
        state deviation</Title> <Definition>The number of events for
        which the absolute value of the FRCE exceeded the maximum
        steady-state frequency deviation.</Definition>
        </CodeDescription>
    :cvar C75: <CodeDescription xmlns=""> <Title>FRCE calculation and
        accuracy descriptor</Title> <Definition>A time series describing
        how FRCE is calculated and its accuracy.</Definition>
        </CodeDescription>
    :cvar C76: <CodeDescription xmlns=""> <Title>Forecasted
        capacity</Title> <Definition>A time series describing forecasted
        capacity.</Definition> </CodeDescription>
    :cvar C77: <CodeDescription xmlns=""> <Title>Minimum available
        capacity</Title> <Definition>A time series describing minimum
        available capacity.</Definition> </CodeDescription>
    :cvar C78: <CodeDescription xmlns=""> <Title>Average available
        capacity</Title> <Definition>A time series describing average
        available capacity.</Definition> </CodeDescription>
    :cvar C79: <CodeDescription xmlns=""> <Title>Maximum available
        capacity</Title> <Definition>A time series describing maximum
        available capacity.</Definition> </CodeDescription>
    :cvar C80: <CodeDescription xmlns=""> <Title>Frequency and accuracy
        descriptor</Title> <Definition>A time series describing how
        system frequency and accuracy are determined.</Definition>
        </CodeDescription>
    :cvar C81: <CodeDescription xmlns=""> <Title>Long-Term internal
        redispatch</Title> <Definition>A time series describing long-
        term redispatch to relieve Scheduling Area internal
        congestion.</Definition> </CodeDescription>
    :cvar C82: <CodeDescription xmlns=""> <Title>Other
        unavailability</Title> <Definition>This is an unplanned
        unavailability. Not considered by market participants as a
        planned maintenance.</Definition> </CodeDescription>
    :cvar C83: <CodeDescription xmlns=""> <Title>Faster than standard
        FAT</Title> <Definition>Bids that can support a �Full Activation
        Time� (FAT) that is faster than standard FAT. Fast activation
        can be done for bids with activation time shorter than the
        minimum requirement for the standard product. When circumstances
        call for it, the TSO can order activation of such bids on a
        shorter notice.</Definition> </CodeDescription>
    :cvar C84: <CodeDescription xmlns=""> <Title>Faster than standard
        deactivation time</Title> <Definition>Fast deactivation can be
        done for bids with activation time shorter than the minimum
        requirement for the standard product. When circumstances call
        for it, the TSO can order activation of such bids on a shorter
        notice.</Definition> </CodeDescription>
    :cvar C85: <CodeDescription xmlns=""> <Title>Slower than standard
        FAT</Title> <Definition>Bids that can support a Full Activation
        Time (FAT) that is slower than standard FAT.</Definition>
        </CodeDescription>
    :cvar C86: <CodeDescription xmlns=""> <Title>Remedial action cost
        summary</Title> <Definition>A timeseries summarizing all
        incurred costs and/or revenues per party related to the
        activated remedial actions eligible to Cost
        Sharing.</Definition> </CodeDescription>
    :cvar C87: <CodeDescription xmlns=""> <Title>Settlement
        result</Title> <Definition>A timeseries representing the cost
        sharing settlement results between parties (i.e. which party
        will be paying and/or receiving money for the concerned
        period).</Definition> </CodeDescription>
    :cvar C88: <CodeDescription xmlns=""> <Title>Reserved cross zonal
        capacity</Title> <Definition>The reserved cross zonal capacity
        for system operator needs (EBGL art. 38(1)(b) and art.
        41.).</Definition> </CodeDescription>
    :cvar C89: <CodeDescription xmlns=""> <Title>Energy reserves</Title>
        <Definition>A timeseries describing energy
        reserves.</Definition> </CodeDescription>
    :cvar C90: <CodeDescription xmlns=""> <Title>Combined dynamic
        constraint</Title> <Definition>The time series describes a
        combined dynamic constraint, being defined as a limit on the sum
        of power flows on a set of network elements or partial flows on
        a set of network elements for the purpose to respect dynamic
        stability limits.</Definition> </CodeDescription>
    :cvar C91: <CodeDescription xmlns=""> <Title>Anonymised
        constraint</Title> <Definition>The time series describes an
        anonymised constraint.</Definition> </CodeDescription>
    :cvar C92: <CodeDescription xmlns=""> <Title>Synchronous condenser
        activation</Title> <Definition>Activates a number of generators
        or other units in synchronous condenser mode.</Definition>
        </CodeDescription>
    :cvar C93: <CodeDescription xmlns=""> <Title>Permission
        administration details</Title> <Definition>A timeseries
        describing permission details such as authorisations, licenses
        or related regulatory requirements.</Definition>
        </CodeDescription>
    :cvar C94: <CodeDescription xmlns=""> <Title>Maximum capacity value
        of AC border flow</Title> <Definition>Maximum flow on an AC
        border between two areas (capacity)</Definition>
        </CodeDescription>
    :cvar C95: <CodeDescription xmlns=""> <Title>Initial forecast value
        of AC border flow</Title> <Definition>Initial flow on an AC
        border between two areas (forecast)</Definition>
        </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"
    A13 = "A13"
    A14 = "A14"
    A15 = "A15"
    A16 = "A16"
    A17 = "A17"
    A18 = "A18"
    A19 = "A19"
    A20 = "A20"
    A21 = "A21"
    A22 = "A22"
    A23 = "A23"
    A24 = "A24"
    A25 = "A25"
    A26 = "A26"
    A27 = "A27"
    A28 = "A28"
    A29 = "A29"
    A30 = "A30"
    A31 = "A31"
    A32 = "A32"
    A33 = "A33"
    A34 = "A34"
    A35 = "A35"
    A36 = "A36"
    A37 = "A37"
    A38 = "A38"
    A40 = "A40"
    A41 = "A41"
    A42 = "A42"
    A43 = "A43"
    A44 = "A44"
    A45 = "A45"
    A46 = "A46"
    A47 = "A47"
    A48 = "A48"
    A49 = "A49"
    A50 = "A50"
    A51 = "A51"
    A52 = "A52"
    A53 = "A53"
    A54 = "A54"
    A55 = "A55"
    A56 = "A56"
    A57 = "A57"
    A58 = "A58"
    A59 = "A59"
    A60 = "A60"
    A61 = "A61"
    A62 = "A62"
    A63 = "A63"
    A64 = "A64"
    A65 = "A65"
    A66 = "A66"
    A67 = "A67"
    A68 = "A68"
    A69 = "A69"
    A70 = "A70"
    A71 = "A71"
    A72 = "A72"
    A73 = "A73"
    A74 = "A74"
    A75 = "A75"
    A76 = "A76"
    A77 = "A77"
    A78 = "A78"
    A79 = "A79"
    A80 = "A80"
    A81 = "A81"
    A82 = "A82"
    A83 = "A83"
    A84 = "A84"
    A85 = "A85"
    A86 = "A86"
    A87 = "A87"
    A88 = "A88"
    A89 = "A89"
    A90 = "A90"
    A91 = "A91"
    A92 = "A92"
    A93 = "A93"
    A94 = "A94"
    A95 = "A95"
    A96 = "A96"
    A97 = "A97"
    A98 = "A98"
    A99 = "A99"
    B01 = "B01"
    B02 = "B02"
    B03 = "B03"
    B04 = "B04"
    B05 = "B05"
    B06 = "B06"
    B07 = "B07"
    B08 = "B08"
    B09 = "B09"
    B10 = "B10"
    B11 = "B11"
    B12 = "B12"
    B13 = "B13"
    B14 = "B14"
    B15 = "B15"
    B16 = "B16"
    B17 = "B17"
    B18 = "B18"
    B19 = "B19"
    B20 = "B20"
    B21 = "B21"
    B22 = "B22"
    B23 = "B23"
    B24 = "B24"
    B25 = "B25"
    B26 = "B26"
    B27 = "B27"
    B28 = "B28"
    B29 = "B29"
    B30 = "B30"
    B31 = "B31"
    B32 = "B32"
    B33 = "B33"
    B34 = "B34"
    B35 = "B35"
    B36 = "B36"
    B37 = "B37"
    B38 = "B38"
    B39 = "B39"
    B40 = "B40"
    B41 = "B41"
    B42 = "B42"
    B43 = "B43"
    B44 = "B44"
    B45 = "B45"
    B46 = "B46"
    B47 = "B47"
    B48 = "B48"
    B49 = "B49"
    B50 = "B50"
    B51 = "B51"
    B52 = "B52"
    B53 = "B53"
    B54 = "B54"
    B55 = "B55"
    B56 = "B56"
    B57 = "B57"
    B58 = "B58"
    B59 = "B59"
    B60 = "B60"
    B61 = "B61"
    B62 = "B62"
    B63 = "B63"
    B64 = "B64"
    B65 = "B65"
    B66 = "B66"
    B67 = "B67"
    B68 = "B68"
    B69 = "B69"
    B70 = "B70"
    B71 = "B71"
    B72 = "B72"
    B73 = "B73"
    B74 = "B74"
    B75 = "B75"
    B76 = "B76"
    B77 = "B77"
    B78 = "B78"
    B79 = "B79"
    B80 = "B80"
    B81 = "B81"
    B82 = "B82"
    B83 = "B83"
    B84 = "B84"
    B85 = "B85"
    B86 = "B86"
    B87 = "B87"
    B88 = "B88"
    B89 = "B89"
    B90 = "B90"
    B91 = "B91"
    B92 = "B92"
    B93 = "B93"
    B94 = "B94"
    B95 = "B95"
    B96 = "B96"
    B97 = "B97"
    B98 = "B98"
    B99 = "B99"
    C01 = "C01"
    C02 = "C02"
    C03 = "C03"
    C04 = "C04"
    C05 = "C05"
    C06 = "C06"
    C07 = "C07"
    C08 = "C08"
    C09 = "C09"
    C10 = "C10"
    C11 = "C11"
    C12 = "C12"
    C13 = "C13"
    C14 = "C14"
    C15 = "C15"
    C16 = "C16"
    C17 = "C17"
    C18 = "C18"
    C19 = "C19"
    C20 = "C20"
    C21 = "C21"
    C22 = "C22"
    C23 = "C23"
    C24 = "C24"
    C25 = "C25"
    C26 = "C26"
    C27 = "C27"
    C28 = "C28"
    C29 = "C29"
    C30 = "C30"
    C31 = "C31"
    C32 = "C32"
    C33 = "C33"
    C34 = "C34"
    C35 = "C35"
    C36 = "C36"
    C37 = "C37"
    C38 = "C38"
    C39 = "C39"
    C40 = "C40"
    C41 = "C41"
    C42 = "C42"
    C43 = "C43"
    C44 = "C44"
    C45 = "C45"
    C46 = "C46"
    C47 = "C47"
    C48 = "C48"
    C49 = "C49"
    C50 = "C50"
    C51 = "C51"
    C52 = "C52"
    C53 = "C53"
    C54 = "C54"
    C55 = "C55"
    C56 = "C56"
    C57 = "C57"
    C58 = "C58"
    C59 = "C59"
    C60 = "C60"
    C61 = "C61"
    C62 = "C62"
    C63 = "C63"
    C64 = "C64"
    C65 = "C65"
    C66 = "C66"
    C67 = "C67"
    C68 = "C68"
    C69 = "C69"
    C70 = "C70"
    C71 = "C71"
    C72 = "C72"
    C73 = "C73"
    C74 = "C74"
    C75 = "C75"
    C76 = "C76"
    C77 = "C77"
    C78 = "C78"
    C79 = "C79"
    C80 = "C80"
    C81 = "C81"
    C82 = "C82"
    C83 = "C83"
    C84 = "C84"
    C85 = "C85"
    C86 = "C86"
    C87 = "C87"
    C88 = "C88"
    C89 = "C89"
    C90 = "C90"
    C91 = "C91"
    C92 = "C92"
    C93 = "C93"
    C94 = "C94"
    C95 = "C95"


class CategoryTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Base</Title>
        <Definition>The auction is for a base period.</Definition>
        </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Peak</Title>
        <Definition>The auction is for a peak period.</Definition>
        </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Off peak</Title>
        <Definition>The auction is for an off peak period.</Definition>
        </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Hourly</Title>
        <Definition>The auction is for an hourly period.</Definition>
        </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"


class ClassificationTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Detail type </Title>
        <Definition>The Time Series content provides detailed
        information.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Summary type </Title>
        <Definition>The Time Series content provides aggregated
        information.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"


class CodingSchemeType(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>EIC</Title>
        <Definition>The coding scheme is the Energy Identification
        Coding Scheme (EIC), maintained by ENTSO-E.</Definition>
        </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>CGM</Title>
        <Definition>The coding scheme used for Common Grid Model
        Exchange Standard (CGMES).</Definition> </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Coding scheme which are
        part of GS1 system</Title> <Definition>The coding schemes
        maintained by GS1.</Definition> </CodeDescription>
    :cvar NAD: <CodeDescription xmlns=""> <Title>Andorra National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NAL: <CodeDescription xmlns=""> <Title>Albania National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NAM: <CodeDescription xmlns=""> <Title>Armenia National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NAT: <CodeDescription xmlns=""> <Title>Austria National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NAZ: <CodeDescription xmlns=""> <Title>Azerbaijan National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NBA: <CodeDescription xmlns=""> <Title>Bosnia and Herzegovina
        National coding scheme</Title> <Definition>The National coding
        scheme of the country in question.</Definition>
        </CodeDescription>
    :cvar NBE: <CodeDescription xmlns=""> <Title>Belgium National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NBG: <CodeDescription xmlns=""> <Title>Bulgaria National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NCH: <CodeDescription xmlns=""> <Title>Switzerland National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NCS: <CodeDescription xmlns=""> <Title>Serbia and Montenegro
        National coding scheme</Title> <Definition>The National coding
        scheme of the country in question.</Definition>
        </CodeDescription>
    :cvar NCY: <CodeDescription xmlns=""> <Title>Cyprus National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NCZ: <CodeDescription xmlns=""> <Title>Czech Republic National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NDE: <CodeDescription xmlns=""> <Title>Germany National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NDK: <CodeDescription xmlns=""> <Title>Denmark National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NEE: <CodeDescription xmlns=""> <Title>Estonia National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NES: <CodeDescription xmlns=""> <Title>Spain National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NFI: <CodeDescription xmlns=""> <Title>Finland National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NFR: <CodeDescription xmlns=""> <Title>France National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NGB: <CodeDescription xmlns=""> <Title>United Kingdom National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NGE: <CodeDescription xmlns=""> <Title>Georgia National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NGI: <CodeDescription xmlns=""> <Title>Gibraltar National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NGR: <CodeDescription xmlns=""> <Title>Greece National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NHR: <CodeDescription xmlns=""> <Title>Croatia National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NHU: <CodeDescription xmlns=""> <Title>Hungary National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NIE: <CodeDescription xmlns=""> <Title>Ireland National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NIT: <CodeDescription xmlns=""> <Title>Italy National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NKG: <CodeDescription xmlns=""> <Title>Kyrgyzstan National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NKZ: <CodeDescription xmlns=""> <Title>Kazakhstan National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NLI: <CodeDescription xmlns=""> <Title>Liechtenstein National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NLT: <CodeDescription xmlns=""> <Title>Lithuania National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NLU: <CodeDescription xmlns=""> <Title>Luxembourg National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NLV: <CodeDescription xmlns=""> <Title>Latvia National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NMA: <CodeDescription xmlns=""> <Title>Morocco National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NMD: <CodeDescription xmlns=""> <Title>Moldavia National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NMK: <CodeDescription xmlns=""> <Title>Macedonia National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NNL: <CodeDescription xmlns=""> <Title>Netherlands National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NNN: <CodeDescription xmlns=""> <Title>Nordic Regional coding
        scheme</Title> <Definition>The coding scheme of the Nordic
        region which covers Denmark, Finland, Norway and
        Sweden.</Definition> </CodeDescription>
    :cvar NNO: <CodeDescription xmlns=""> <Title>Norway National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NPL: <CodeDescription xmlns=""> <Title>Poland National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NPT: <CodeDescription xmlns=""> <Title>Portugal National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NRO: <CodeDescription xmlns=""> <Title>Romania National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NRU: <CodeDescription xmlns=""> <Title>Russian Federation
        National coding scheme</Title> <Definition>The National coding
        scheme of the country in question.</Definition>
        </CodeDescription>
    :cvar NSE: <CodeDescription xmlns=""> <Title>Sweden National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NSI: <CodeDescription xmlns=""> <Title>Slovenia National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NSK: <CodeDescription xmlns=""> <Title>Slovakia National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NTR: <CodeDescription xmlns=""> <Title>Turkey National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NUA: <CodeDescription xmlns=""> <Title>Ukraine National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A10 = "A10"
    NAD = "NAD"
    NAL = "NAL"
    NAM = "NAM"
    NAT = "NAT"
    NAZ = "NAZ"
    NBA = "NBA"
    NBE = "NBE"
    NBG = "NBG"
    NCH = "NCH"
    NCS = "NCS"
    NCY = "NCY"
    NCZ = "NCZ"
    NDE = "NDE"
    NDK = "NDK"
    NEE = "NEE"
    NES = "NES"
    NFI = "NFI"
    NFR = "NFR"
    NGB = "NGB"
    NGE = "NGE"
    NGI = "NGI"
    NGR = "NGR"
    NHR = "NHR"
    NHU = "NHU"
    NIE = "NIE"
    NIT = "NIT"
    NKG = "NKG"
    NKZ = "NKZ"
    NLI = "NLI"
    NLT = "NLT"
    NLU = "NLU"
    NLV = "NLV"
    NMA = "NMA"
    NMD = "NMD"
    NMK = "NMK"
    NNL = "NNL"
    NNN = "NNN"
    NNO = "NNO"
    NPL = "NPL"
    NPT = "NPT"
    NRO = "NRO"
    NRU = "NRU"
    NSE = "NSE"
    NSI = "NSI"
    NSK = "NSK"
    NTR = "NTR"
    NUA = "NUA"


class CodingSchemeTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>EIC</Title>
        <Definition>The coding scheme is the Energy Identification
        Coding Scheme (EIC), maintained by ENTSO-E.</Definition>
        </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>CGM</Title>
        <Definition>The coding scheme used for Common Grid Model
        Exchange Standard (CGMES).</Definition> </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Coding scheme which are
        part of GS1 system</Title> <Definition>The coding schemes
        maintained by GS1.</Definition> </CodeDescription>
    :cvar NAD: <CodeDescription xmlns=""> <Title>Andorra National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NAL: <CodeDescription xmlns=""> <Title>Albania National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NAM: <CodeDescription xmlns=""> <Title>Armenia National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NAT: <CodeDescription xmlns=""> <Title>Austria National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NAZ: <CodeDescription xmlns=""> <Title>Azerbaijan National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NBA: <CodeDescription xmlns=""> <Title>Bosnia and Herzegovina
        National coding scheme</Title> <Definition>The National coding
        scheme of the country in question.</Definition>
        </CodeDescription>
    :cvar NBE: <CodeDescription xmlns=""> <Title>Belgium National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NBG: <CodeDescription xmlns=""> <Title>Bulgaria National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NCH: <CodeDescription xmlns=""> <Title>Switzerland National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NCS: <CodeDescription xmlns=""> <Title>Serbia and Montenegro
        National coding scheme</Title> <Definition>The National coding
        scheme of the country in question.</Definition>
        </CodeDescription>
    :cvar NCY: <CodeDescription xmlns=""> <Title>Cyprus National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NCZ: <CodeDescription xmlns=""> <Title>Czech Republic National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NDE: <CodeDescription xmlns=""> <Title>Germany National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NDK: <CodeDescription xmlns=""> <Title>Denmark National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NEE: <CodeDescription xmlns=""> <Title>Estonia National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NES: <CodeDescription xmlns=""> <Title>Spain National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NFI: <CodeDescription xmlns=""> <Title>Finland National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NFR: <CodeDescription xmlns=""> <Title>France National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NGB: <CodeDescription xmlns=""> <Title>United Kingdom National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NGE: <CodeDescription xmlns=""> <Title>Georgia National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NGI: <CodeDescription xmlns=""> <Title>Gibraltar National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NGR: <CodeDescription xmlns=""> <Title>Greece National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NHR: <CodeDescription xmlns=""> <Title>Croatia National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NHU: <CodeDescription xmlns=""> <Title>Hungary National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NIE: <CodeDescription xmlns=""> <Title>Ireland National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NIT: <CodeDescription xmlns=""> <Title>Italy National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NKG: <CodeDescription xmlns=""> <Title>Kyrgyzstan National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NKZ: <CodeDescription xmlns=""> <Title>Kazakhstan National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NLI: <CodeDescription xmlns=""> <Title>Liechtenstein National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NLT: <CodeDescription xmlns=""> <Title>Lithuania National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NLU: <CodeDescription xmlns=""> <Title>Luxembourg National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NLV: <CodeDescription xmlns=""> <Title>Latvia National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NMA: <CodeDescription xmlns=""> <Title>Morocco National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NMD: <CodeDescription xmlns=""> <Title>Moldavia National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NMK: <CodeDescription xmlns=""> <Title>Macedonia National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NNL: <CodeDescription xmlns=""> <Title>Netherlands National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NNN: <CodeDescription xmlns=""> <Title>Nordic Regional coding
        scheme</Title> <Definition>The coding scheme of the Nordic
        region which covers Denmark, Finland, Norway and
        Sweden.</Definition> </CodeDescription>
    :cvar NNO: <CodeDescription xmlns=""> <Title>Norway National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NPL: <CodeDescription xmlns=""> <Title>Poland National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NPT: <CodeDescription xmlns=""> <Title>Portugal National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NRO: <CodeDescription xmlns=""> <Title>Romania National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NRU: <CodeDescription xmlns=""> <Title>Russian Federation
        National coding scheme</Title> <Definition>The National coding
        scheme of the country in question.</Definition>
        </CodeDescription>
    :cvar NSE: <CodeDescription xmlns=""> <Title>Sweden National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NSI: <CodeDescription xmlns=""> <Title>Slovenia National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NSK: <CodeDescription xmlns=""> <Title>Slovakia National
        coding scheme</Title> <Definition>The National coding scheme of
        the country in question.</Definition> </CodeDescription>
    :cvar NTR: <CodeDescription xmlns=""> <Title>Turkey National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    :cvar NUA: <CodeDescription xmlns=""> <Title>Ukraine National coding
        scheme</Title> <Definition>The National coding scheme of the
        country in question.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A10 = "A10"
    NAD = "NAD"
    NAL = "NAL"
    NAM = "NAM"
    NAT = "NAT"
    NAZ = "NAZ"
    NBA = "NBA"
    NBE = "NBE"
    NBG = "NBG"
    NCH = "NCH"
    NCS = "NCS"
    NCY = "NCY"
    NCZ = "NCZ"
    NDE = "NDE"
    NDK = "NDK"
    NEE = "NEE"
    NES = "NES"
    NFI = "NFI"
    NFR = "NFR"
    NGB = "NGB"
    NGE = "NGE"
    NGI = "NGI"
    NGR = "NGR"
    NHR = "NHR"
    NHU = "NHU"
    NIE = "NIE"
    NIT = "NIT"
    NKG = "NKG"
    NKZ = "NKZ"
    NLI = "NLI"
    NLT = "NLT"
    NLU = "NLU"
    NLV = "NLV"
    NMA = "NMA"
    NMD = "NMD"
    NMK = "NMK"
    NNL = "NNL"
    NNN = "NNN"
    NNO = "NNO"
    NPL = "NPL"
    NPT = "NPT"
    NRO = "NRO"
    NRU = "NRU"
    NSE = "NSE"
    NSI = "NSI"
    NSK = "NSK"
    NTR = "NTR"
    NUA = "NUA"


class ContractTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Daily contract</Title>
        <Definition>The condition under which capacity is allocated and
        handled is by daily auction or a daily transmission allocation
        procedure.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Weekly contract</Title>
        <Definition>The condition under which capacity is allocated and
        handled is by weekly auction or a weekly transmission allocation
        procedure.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Monthly
        contract</Title> <Definition>The condition under which capacity
        is allocated and handled is by monthly auction or a monthly
        transmission allocation procedure.</Definition>
        </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Yearly contract</Title>
        <Definition>The condition under which capacity is allocated and
        handled is by yearly auction or a yearly transmission allocation
        procedure.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Total contract</Title>
        <Definition>This is the sum of all capacity contract types for
        the period covered.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Long term
        contract</Title> <Definition>The condition under which capacity
        is allocated and handled is by long term trade agreements
        according to European regulations (EU Directive
        1228/2003).</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Intraday
        contract</Title> <Definition>The condition under which the
        capacity is allocated and handled is through an intraday auction
        and allocation process.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Quarter yearly
        contract</Title> <Definition>The condition under which capacity
        is allocated and handled is by quarter yearly auction or a
        quarter yearly transmission allocation procedure.</Definition>
        </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>Semestrial
        contract</Title> <Definition>The condition under which capacity
        is allocated and handled is by half yearly auction or a half
        yearly transmission allocation procedure.</Definition>
        </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Multiple year
        contract</Title> <Definition>The condition under which capacity
        is allocated and handled is by multiple year
        auctions.</Definition> </CodeDescription>
    :cvar A11: <CodeDescription xmlns=""> <Title>Intraday balancing
        mechanism contract</Title> <Definition>The condition under which
        the capacity is allocated and handled is through intraday energy
        balancing services.</Definition> </CodeDescription>
    :cvar A12: <CodeDescription xmlns=""> <Title>Historical
        contract</Title> <Definition>A Contract established before the
        EU directive that are valid until the term of the
        contract.</Definition> </CodeDescription>
    :cvar A13: <CodeDescription xmlns=""> <Title>Hourly contract</Title>
        <Definition>The condition under which capacity is allocated and
        handled is by hourly auctions.</Definition> </CodeDescription>
    :cvar A14: <CodeDescription xmlns=""> <Title>First intraday auction
        contract</Title> <Definition>The first intraday auction contract
        (IDA1).</Definition> </CodeDescription>
    :cvar A15: <CodeDescription xmlns=""> <Title>Second intraday auction
        contract</Title> <Definition>The second intraday auction
        contract (IDA2).</Definition> </CodeDescription>
    :cvar A16: <CodeDescription xmlns=""> <Title>Third intraday auction
        contract</Title> <Definition>The third intraday auction contract
        (IDA3).</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"
    A13 = "A13"
    A14 = "A14"
    A15 = "A15"
    A16 = "A16"


class CoordinateSystemTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>ED50</Title>
        <Definition>ED 50 (European Datum 1950) is a geodetic datum
        which was defined after World War II for the international
        connection of geodetic networks.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>OSGB36</Title>
        <Definition>Ordinance Survey Great Britain 1936. The Ordinance
        Survey (OS) devised the national grid reference system, and it
        is heavily used in their survey data, and in maps (whether
        published by the Ordinance Survey or commercial map producers)
        based on those surveys.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>WGS84</Title>
        <Definition>The World Geodetic System version 1984. for use in
        cartography, geodesy, and navigation including by GPS. It
        comprises a standard coordinate system for the earth, a standard
        spheroidal reference surface (the datum or reference ellipsoid)
        for raw altitude data, and a gravitational equipotential surface
        (the geoid) that defines the nominal sea level.</Definition>
        </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>GTRF</Title>
        <Definition>Galileo Terrestrial Reference Frame</Definition>
        </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"


class CurrencyTypeList(Enum):
    """
    :cvar BAM: <CodeDescription xmlns=""> <Title>Bosnian convertible
        marka</Title> <Definition>The Legal tender of Bosnia and
        Herzegovina.</Definition> </CodeDescription>
    :cvar BGN: <CodeDescription xmlns=""> <Title>Bulgarian lev</Title>
        <Definition>The Legal tender of Bulgaria.</Definition>
        </CodeDescription>
    :cvar CHF: <CodeDescription xmlns=""> <Title>Swiss Franc</Title>
        <Definition>The Legal tender of Switzerland.</Definition>
        </CodeDescription>
    :cvar CZK: <CodeDescription xmlns=""> <Title>Czech Koruna</Title>
        <Definition>The legal tender of the Czech Republic.</Definition>
        </CodeDescription>
    :cvar DKK: <CodeDescription xmlns=""> <Title>Danish Kroner </Title>
        <Definition>The Legal tender of Denmark.</Definition>
        </CodeDescription>
    :cvar EUR: <CodeDescription xmlns=""> <Title>EURO</Title>
        <Definition>The European legal tender.</Definition>
        </CodeDescription>
    :cvar GBP: <CodeDescription xmlns=""> <Title>Pound Sterling</Title>
        <Definition>The Legal tender of the United Kingdom.</Definition>
        </CodeDescription>
    :cvar HRK: <CodeDescription xmlns=""> <Title>Croatian kuna</Title>
        <Definition>The legal tender of Croatia.</Definition>
        </CodeDescription>
    :cvar HUF: <CodeDescription xmlns=""> <Title>Hungarian
        Forint</Title> <Definition>The Legal tender of
        Hungary.</Definition> </CodeDescription>
    :cvar ISK: <CodeDescription xmlns=""> <Title>Icelandic krona</Title>
        <Definition>The Legal tender of Iceland.</Definition>
        </CodeDescription>
    :cvar LEK: <CodeDescription xmlns=""> <Title>Albanian lek</Title>
        <Definition>The Legal tender of Albania.</Definition>
        </CodeDescription>
    :cvar LTL: <CodeDescription xmlns=""> <Title>Lithuanian
        litas</Title> <Definition>The Legal tender of
        Lithuania</Definition> </CodeDescription>
    :cvar MKD: <CodeDescription xmlns=""> <Title>Macedonian
        denar</Title> <Definition>The Legal tender of
        FYROM.</Definition> </CodeDescription>
    :cvar NOK: <CodeDescription xmlns=""> <Title>Norwegian Kroner
        </Title> <Definition>The Legal tender of Norway.</Definition>
        </CodeDescription>
    :cvar PLN: <CodeDescription xmlns=""> <Title>Polish zloty</Title>
        <Definition>The Legal tender of Poland.</Definition>
        </CodeDescription>
    :cvar RON: <CodeDescription xmlns=""> <Title>Romanian Leu</Title>
        <Definition>The Legal tender of Romania.</Definition>
        </CodeDescription>
    :cvar RSD: <CodeDescription xmlns=""> <Title>Serbian dinar</Title>
        <Definition>The Legal tender of Serbian Republic.</Definition>
        </CodeDescription>
    :cvar SAR: <CodeDescription xmlns=""> <Title>Saudi Arabian
        Riyal</Title> <Definition>The Legal tender of Saudi
        Arabia.</Definition> </CodeDescription>
    :cvar SEK: <CodeDescription xmlns=""> <Title>Swedish kroner</Title>
        <Definition>The Legal tender of Sweden.</Definition>
        </CodeDescription>
    :cvar SKK: <CodeDescription xmlns=""> <Title>Slovak Koruna</Title>
        <Definition>The legal tender of Slovakia.</Definition>
        </CodeDescription>
    :cvar TRY: <CodeDescription xmlns=""> <Title>New Turkish
        Lira</Title> <Definition>The Legal tender of
        Turkey.</Definition> </CodeDescription>
    :cvar UAH: <CodeDescription xmlns=""> <Title>Ukrainian
        hryvnia</Title> <Definition>The legal tender of
        Ukraine.</Definition> </CodeDescription>
    :cvar USD: <CodeDescription xmlns=""> <Title>US Dollar</Title>
        <Definition>The legal tender of the USA.</Definition>
        </CodeDescription>
    """

    BAM = "BAM"
    BGN = "BGN"
    CHF = "CHF"
    CZK = "CZK"
    DKK = "DKK"
    EUR = "EUR"
    GBP = "GBP"
    HRK = "HRK"
    HUF = "HUF"
    ISK = "ISK"
    LEK = "LEK"
    LTL = "LTL"
    MKD = "MKD"
    NOK = "NOK"
    PLN = "PLN"
    RON = "RON"
    RSD = "RSD"
    SAR = "SAR"
    SEK = "SEK"
    SKK = "SKK"
    TRY = "TRY"
    UAH = "UAH"
    USD = "USD"


class CurveTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Sequential fixed size
        block</Title> <Definition>The curve is made of successive
        Intervals of time (Blocks) of constant duration (size), where
        the size of the Blocks is equal to the Resolution of the
        Period.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Point</Title>
        <Definition>The curve is made of successive instants of time
        (Points).</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Variable sized
        Block</Title> <Definition>The curve is made of successive
        Intervals of time (Blocks) of variable duration (size), where
        the end date and end time of each Block are equal to the start
        date and start time of the next Interval. For the last Block the
        end date and end time of the last Interval would be equal to
        EndDateTime of TimeInterval.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Overlapping
        breakpoint</Title> <Definition>The curve is made of successive
        Intervals of time of variable duration (size), where the end
        date and end time of each interval are equal to the start date
        and start time of the next Interval.</Definition>
        </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Non-overlapping
        breakpoint</Title> <Definition>This curve is a restriction of
        the curve type A04, i.e. overlapping breakpoints. The
        restriction is that a single Period is allowed.</Definition>
        </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"


class DirectionTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>UP</Title>
        <Definition>Up signifies that the available power can be used by
        the Purchasing area to increase energy.</Definition>
        </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>DOWN</Title>
        <Definition>Down signifies that the available power can be used
        by the Purchasing area to decrease energy.</Definition>
        </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>UP and DOWN</Title>
        <Definition>Up and Down signifies that the UP and Down values
        are equal.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Stable</Title>
        <Definition>The direction at a given instant in time is
        considered to be stable.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"


class DocumentTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Balance responsible
        schedule</Title> <Definition>A schedule which has been prepared
        by a balance responsible party providing planned schedule
        information.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Allocated capacity
        schedule</Title> <Definition>A schedule which has been prepared
        by a capacity allocator providing allocated
        capacity.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Balance area
        schedule</Title> <Definition>A schedule that provides the
        planned schedule information for a balance area.</Definition>
        </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>System Operator area
        schedule</Title> <Definition>A compilation of all external
        schedules concerning two System Operator areas of all balance
        responsible parties.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Control block area
        schedule</Title> <Definition>A compilation of all the exchange
        programs of all control areas for one control block with all
        neighbouring control areas of a neighbouring control
        block.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Coordination center
        area schedule</Title> <Definition>A compilation of the exchange
        programs of all exchange blocks divided into UCTE south and
        north.</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Intermediate
        confirmation report</Title> <Definition>An intermediate
        confirmation report that may be produced between final
        cutoffs.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Final confirmation
        report</Title> <Definition>A final confirmation report that is
        produced after a final cutoff.</Definition> </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>Finalised
        schedule</Title> <Definition>A compilation of a set of schedules
        that have been finalized after a given cutoff.</Definition>
        </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Regulation data
        report</Title> <Definition>A compilation of the time series
        employed on a given day to ensure the balance of the
        system.</Definition> </CodeDescription>
    :cvar A11: <CodeDescription xmlns=""> <Title>Aggregated energy data
        report</Title> <Definition>A compilation of the time series of
        all the meter readings or their equivalent for a given
        period.</Definition> </CodeDescription>
    :cvar A12: <CodeDescription xmlns=""> <Title>Imbalance
        report</Title> <Definition>The report containing the complete
        situation of a given period for a party and including the
        schedules, regulation data and actual or calculated
        readings.</Definition> </CodeDescription>
    :cvar A13: <CodeDescription xmlns=""> <Title>Interconnection
        Capacity</Title> <Definition>Document for cross-border capacity
        exchanges.</Definition> </CodeDescription>
    :cvar A14: <CodeDescription xmlns=""> <Title>Resource Provider
        Resource Schedule</Title> <Definition>A document providing the
        schedules for resource objects submitted by a resource
        provider.</Definition> </CodeDescription>
    :cvar A15: <CodeDescription xmlns=""> <Title>Acquiring System
        Operator Reserve Schedule</Title> <Definition>A document
        providing reserve purchases submitted by an Acquiring System
        Operator.</Definition> </CodeDescription>
    :cvar A16: <CodeDescription xmlns=""> <Title>Anomaly Report</Title>
        <Definition>A document providing anomaly information for the
        receiving party to correct.</Definition> </CodeDescription>
    :cvar A17: <CodeDescription xmlns=""> <Title>Acknowledgement
        Document</Title> <Definition>A document providing
        acknowledgement information.</Definition> </CodeDescription>
    :cvar A18: <CodeDescription xmlns=""> <Title>Confirmation
        report</Title> <Definition>A document providing confirmation
        information.</Definition> </CodeDescription>
    :cvar A19: <CodeDescription xmlns=""> <Title>Capacity for
        Resale</Title> <Definition>A document providing information
        about capacity for resale.</Definition> </CodeDescription>
    :cvar A20: <CodeDescription xmlns=""> <Title>Approved Capacity
        Transfer</Title> <Definition>A document to approve a capacity
        transfer.</Definition> </CodeDescription>
    :cvar A21: <CodeDescription xmlns=""> <Title>Capacity transfer
        notification</Title> <Definition>A document notifying a capacity
        transfer.</Definition> </CodeDescription>
    :cvar A22: <CodeDescription xmlns=""> <Title>Transmission rights
        portfolio</Title> <Definition>A document providing the portfolio
        of the transmission capacity rights of a market
        participant.</Definition> </CodeDescription>
    :cvar A23: <CodeDescription xmlns=""> <Title>Allocations</Title>
        <Definition>A document providing the capacity allocations for a
        border.</Definition> </CodeDescription>
    :cvar A24: <CodeDescription xmlns=""> <Title>Bid document</Title>
        <Definition>A document providing bid information.</Definition>
        </CodeDescription>
    :cvar A25: <CodeDescription xmlns=""> <Title>Allocation result
        document</Title> <Definition>A document providing the allocation
        results of an auction.</Definition> </CodeDescription>
    :cvar A26: <CodeDescription xmlns=""> <Title>Capacity
        document</Title> <Definition>A document providing capacity
        information.</Definition> </CodeDescription>
    :cvar A27: <CodeDescription xmlns=""> <Title>Rights document</Title>
        <Definition>A document providing transmission capacity rights
        information.</Definition> </CodeDescription>
    :cvar A28: <CodeDescription xmlns=""> <Title>Generation availability
        schedule</Title> <Definition>This document contains information
        related to energy availability.</Definition> </CodeDescription>
    :cvar A30: <CodeDescription xmlns=""> <Title>Cross border
        schedule</Title> <Definition>This document contains the cross
        border schedules for all the borders of a given country where
        energy is exchanged.</Definition> </CodeDescription>
    :cvar A31: <CodeDescription xmlns=""> <Title>Agreed capacity</Title>
        <Definition>The capacity agreed between parties.</Definition>
        </CodeDescription>
    :cvar A32: <CodeDescription xmlns=""> <Title>Proposed
        capacity</Title> <Definition>The capacity proposed for agreement
        between parties.</Definition> </CodeDescription>
    :cvar A33: <CodeDescription xmlns=""> <Title>System vertical
        load</Title> <Definition>The sum of all flows out of the
        transmission grid via directly connected transformers and lines
        to distribution grids and end consumers as known by the System
        Operator.</Definition> </CodeDescription>
    :cvar A34: <CodeDescription xmlns=""> <Title>Escalation
        document</Title> <Definition>A document which requesting the
        escalation of a situation.</Definition> </CodeDescription>
    :cvar A35: <CodeDescription xmlns=""> <Title>Trouble shooting
        document</Title> <Definition>A document providing trouble
        shooting information for the resolution of a
        problem.</Definition> </CodeDescription>
    :cvar A36: <CodeDescription xmlns=""> <Title>Deactivation
        document</Title> <Definition>The capacity proposed for agreement
        between parties.</Definition> </CodeDescription>
    :cvar A37: <CodeDescription xmlns=""> <Title>Reserve tender
        document</Title> <Definition>The document that is used for the
        tendering for reserves within the ERRP process.</Definition>
        </CodeDescription>
    :cvar A38: <CodeDescription xmlns=""> <Title>Reserve Allocation
        Result Document</Title> <Definition>The document used to provide
        the results of a Reserve auction.</Definition>
        </CodeDescription>
    :cvar A39: <CodeDescription xmlns=""> <Title>SATCR
        activation</Title> <Definition>The document is used to provide
        the activation of reserves through the SATCR
        process.</Definition> </CodeDescription>
    :cvar A40: <CodeDescription xmlns=""> <Title>DATCR
        activation</Title> <Definition>The document is used to provide
        the activation of reserves through the DATCR
        process.</Definition> </CodeDescription>
    :cvar A41: <CodeDescription xmlns=""> <Title>Activation
        response</Title> <Definition>The document is used to provide a
        response to a request to activate reserves.</Definition>
        </CodeDescription>
    :cvar A42: <CodeDescription xmlns=""> <Title>Tender
        reduction</Title> <Definition>The document is used to provide
        information concerning the reduction of a previously submitted
        tender.</Definition> </CodeDescription>
    :cvar A43: <CodeDescription xmlns=""> <Title>MOL Document</Title>
        <Definition>The document is used to provide Merit Order List
        information.</Definition> </CodeDescription>
    :cvar A44: <CodeDescription xmlns=""> <Title>Price Document</Title>
        <Definition>The document is used to provide market spot price
        information.</Definition> </CodeDescription>
    :cvar A45: <CodeDescription xmlns=""> <Title>Measurement Value
        Document</Title> <Definition>The document is used to provide
        measurement information from measurement devices.</Definition>
        </CodeDescription>
    :cvar A46: <CodeDescription xmlns=""> <Title>SOAM Document</Title>
        <Definition>The document is used to provide system operator
        accounting data for matching.</Definition> </CodeDescription>
    :cvar A47: <CodeDescription xmlns=""> <Title>SOVA Document</Title>
        <Definition>The document is used to provide system operator
        validated accounting data.</Definition> </CodeDescription>
    :cvar A48: <CodeDescription xmlns=""> <Title>CCVA Document</Title>
        <Definition>The document is used to provide coordination center
        validated accounting data.</Definition> </CodeDescription>
    :cvar A49: <CodeDescription xmlns=""> <Title>Daily settlement
        document</Title> <Definition>The document is used to provide
        daily settlement information.</Definition> </CodeDescription>
    :cvar A50: <CodeDescription xmlns=""> <Title>Weekly settlement
        document</Title> <Definition>The document is used to provide
        weekly settlement information.</Definition> </CodeDescription>
    :cvar A51: <CodeDescription xmlns=""> <Title>Capacity Auction
        Specification Document</Title> <Definition>The document is used
        to provide capacity auction specification
        information.</Definition> </CodeDescription>
    :cvar A52: <CodeDescription xmlns=""> <Title>Market Coupling Results
        Document</Title> <Definition>The document is used to provide the
        results of a market coupling auction.</Definition>
        </CodeDescription>
    :cvar A53: <CodeDescription xmlns=""> <Title>Outage publication
        Document</Title> <Definition>The document is used to provide the
        outage information for publication.</Definition>
        </CodeDescription>
    :cvar A54: <CodeDescription xmlns=""> <Title>Forced generation
        outage Document</Title> <Definition>A document providing
        information on forced generation outages.</Definition>
        </CodeDescription>
    :cvar A55: <CodeDescription xmlns=""> <Title>Summarised Market
        Schedule</Title> <Definition>A compilation of all external
        schedules concerning two Market Balance Areas of all balance
        responsible parties.</Definition> </CodeDescription>
    :cvar A56: <CodeDescription xmlns=""> <Title>Compensation Program
        Schedule</Title> <Definition>A schedule that provides the
        schedule information for the compensation of unintended
        deviation.</Definition> </CodeDescription>
    :cvar A57: <CodeDescription xmlns=""> <Title>Load Frequency Control
        Program Schedule</Title> <Definition>A schedule that provides
        the schedule information for the Load Frequency Control Program
        of a Control Area or a Control Block.</Definition>
        </CodeDescription>
    :cvar A58: <CodeDescription xmlns=""> <Title>Timeframe Independent
        Schedule</Title> <Definition>A compilation of all external
        Timeframe Independent Schedules concerning two System
        Operators.</Definition> </CodeDescription>
    :cvar A59: <CodeDescription xmlns=""> <Title>Status request for a
        status within a process</Title> <Definition>A status request
        being made concerning the status of information within the
        context of a specific ongoing process.</Definition>
        </CodeDescription>
    :cvar A60: <CodeDescription xmlns=""> <Title>status request for a
        position independently from a specific process</Title>
        <Definition>A status request concerning the position of an
        object independently of any ongoing processes.</Definition>
        </CodeDescription>
    :cvar A61: <CodeDescription xmlns=""> <Title>Estimated Net Transfer
        Capacity</Title> <Definition>The estimated net transfer capacity
        for a given border.</Definition> </CodeDescription>
    :cvar A62: <CodeDescription xmlns=""> <Title>Compensation
        rights</Title> <Definition>The capacity rights that have been
        allocated as compensation.</Definition> </CodeDescription>
    :cvar A63: <CodeDescription xmlns=""> <Title>Redispatch
        notice</Title> <Definition>A notice to confirm the actions
        agreed between System Operators to resolve a congestion
        situation through redispatch.</Definition> </CodeDescription>
    :cvar A64: <CodeDescription xmlns=""> <Title>Tender reduction
        response</Title> <Definition>A response to a tender reduction
        request that provides  corrections to the initial
        document.</Definition> </CodeDescription>
    :cvar A65: <CodeDescription xmlns=""> <Title>System total
        load</Title> <Definition>Total load', including losses without
        power used for energy storage, is equal to generation deducted
        with exports, added with imports and deducted with power used
        for energy storage.</Definition> </CodeDescription>
    :cvar A66: <CodeDescription xmlns=""> <Title>Final MOL</Title>
        <Definition>A document providing the information concerning the
        situation of the MOL at the end of an activation
        period.</Definition> </CodeDescription>
    :cvar A67: <CodeDescription xmlns=""> <Title>Resource Provider
        Schedule for production/consumption</Title> <Definition>A
        document providing the schedules for production/consumption for
        resource objects submitted by a resource provider.</Definition>
        </CodeDescription>
    :cvar A68: <CodeDescription xmlns=""> <Title>Installed generation
        per type</Title> <Definition>A document providing the installed
        generation per generation type.</Definition> </CodeDescription>
    :cvar A69: <CodeDescription xmlns=""> <Title>Wind and solar
        forecast</Title> <Definition>A document providing the forecast
        of wind and solar generation.</Definition> </CodeDescription>
    :cvar A70: <CodeDescription xmlns=""> <Title>Load forecast
        margin</Title> <Definition>A document providing the load
        forecast margin for a period.</Definition> </CodeDescription>
    :cvar A71: <CodeDescription xmlns=""> <Title>Generation
        forecast</Title> <Definition>A document providing the generation
        forecast for a period.</Definition> </CodeDescription>
    :cvar A72: <CodeDescription xmlns=""> <Title>Reservoir filling
        information</Title> <Definition>A document providing information
        concerning the filling of reservoirs.</Definition>
        </CodeDescription>
    :cvar A73: <CodeDescription xmlns=""> <Title>Actual
        generation</Title> <Definition>A document providing the actual
        generation for a period.</Definition> </CodeDescription>
    :cvar A74: <CodeDescription xmlns=""> <Title>Wind and solar
        generation</Title> <Definition>A document providing the
        generation of wind and solar energy for a period.</Definition>
        </CodeDescription>
    :cvar A75: <CodeDescription xmlns=""> <Title>Actual generation per
        type</Title> <Definition>A document providing the actual
        generation per generation type for a period.</Definition>
        </CodeDescription>
    :cvar A76: <CodeDescription xmlns=""> <Title>Load
        unavailability</Title> <Definition>A document providing the
        unavailability of units providing load on the
        network.</Definition> </CodeDescription>
    :cvar A77: <CodeDescription xmlns=""> <Title>Production
        unavailability</Title> <Definition>A document providing the
        unavailability of production units providing energy to the
        network.</Definition> </CodeDescription>
    :cvar A78: <CodeDescription xmlns=""> <Title>Transmission
        unavailability</Title> <Definition>A document providing the
        unavailability of transmission capacity on the
        network.</Definition> </CodeDescription>
    :cvar A79: <CodeDescription xmlns=""> <Title>Offshore grid
        infrastructure unavailability</Title> <Definition>A document
        providing the unavailability of an offshore grid infrastructure
        to the network.</Definition> </CodeDescription>
    :cvar A80: <CodeDescription xmlns=""> <Title>Generation
        unavailability</Title> <Definition>A document providing the
        unavailability of generation units providing energy to the
        network.</Definition> </CodeDescription>
    :cvar A81: <CodeDescription xmlns=""> <Title>Contracted
        reserves</Title> <Definition>A document providing the reserves
        contracted for a period.</Definition> </CodeDescription>
    :cvar A82: <CodeDescription xmlns=""> <Title>Accepted offers</Title>
        <Definition>A document providing the offers of reserves that
        have been accepted for a period.</Definition> </CodeDescription>
    :cvar A83: <CodeDescription xmlns=""> <Title>Activated balancing
        quantities</Title> <Definition>A document providing the
        quantities of reserves that have been activated for
        balancing.</Definition> </CodeDescription>
    :cvar A84: <CodeDescription xmlns=""> <Title>Activated balancing
        prices</Title> <Definition>A document providing the prices of
        the reserves that have been activated for
        balancing.</Definition> </CodeDescription>
    :cvar A85: <CodeDescription xmlns=""> <Title>Imbalance
        prices</Title> <Definition>A document providing the prices of
        reserves due to imbalance for a period.</Definition>
        </CodeDescription>
    :cvar A86: <CodeDescription xmlns=""> <Title>Imbalance
        volume</Title> <Definition>A document providing the volume of
        the imbalance for a period.</Definition> </CodeDescription>
    :cvar A87: <CodeDescription xmlns=""> <Title>Financial
        situation</Title> <Definition>A document providing the financial
        situation for reserves.</Definition> </CodeDescription>
    :cvar A88: <CodeDescription xmlns=""> <Title>Cross border
        balancing</Title> <Definition>A document providing the cross
        border balancing requirements for a period.</Definition>
        </CodeDescription>
    :cvar A89: <CodeDescription xmlns=""> <Title>Contracted reserve
        prices</Title> <Definition>A document providing the price of
        reserves contracted for a period.</Definition>
        </CodeDescription>
    :cvar A90: <CodeDescription xmlns=""> <Title>Interconnection network
        expansion</Title> <Definition>A document providing information
        on the expansion of the interconnection network.</Definition>
        </CodeDescription>
    :cvar A91: <CodeDescription xmlns=""> <Title>Counter trade
        notice</Title> <Definition>A document providing information on
        counter trades for a period.</Definition> </CodeDescription>
    :cvar A92: <CodeDescription xmlns=""> <Title>Congestion
        costs</Title> <Definition>A document providing the cost of
        congestion for a period.</Definition> </CodeDescription>
    :cvar A93: <CodeDescription xmlns=""> <Title>DC link
        capacity</Title> <Definition>A document providing the DC links
        for a period.</Definition> </CodeDescription>
    :cvar A94: <CodeDescription xmlns=""> <Title>Non EU
        allocations</Title> <Definition>A document providing allocations
        made to non EU member states.</Definition> </CodeDescription>
    :cvar A95: <CodeDescription xmlns=""> <Title>Configuration
        document</Title> <Definition>A document providing configuration
        information for the network.</Definition> </CodeDescription>
    :cvar A96: <CodeDescription xmlns=""> <Title>Redispatch activation
        document</Title> <Definition>A document enabling the activation
        of a redispatch notice.</Definition> </CodeDescription>
    :cvar A97: <CodeDescription xmlns=""> <Title>Detailed activation
        history document</Title> <Definition>A document enabling a
        detailed history of activations.</Definition> </CodeDescription>
    :cvar A98: <CodeDescription xmlns=""> <Title>Aggregated activation
        history document</Title> <Definition>A document enabling an
        aggregated history of activations.</Definition>
        </CodeDescription>
    :cvar A99: <CodeDescription xmlns=""> <Title>HVDC Link
        constraints</Title> <Definition>A document providing the
        information concerning the maximum and minimum active power flow
        through each link can limited.</Definition> </CodeDescription>
    :cvar B01: <CodeDescription xmlns=""> <Title>HVDC
        Configuration</Title> <Definition>A document providing the
        information concerning the power set point. The mode in which
        the  HVDC is managed.</Definition> </CodeDescription>
    :cvar B02: <CodeDescription xmlns=""> <Title>HVDC Schedule</Title>
        <Definition>A document providing the information for operating
        DC links.</Definition> </CodeDescription>
    :cvar B03: <CodeDescription xmlns=""> <Title>EIC code
        request</Title> <Definition>A document providing the information
        requesting a new EIC code.</Definition> </CodeDescription>
    :cvar B04: <CodeDescription xmlns=""> <Title>EIC code
        information</Title> <Definition>A document providing EIC
        information  in a central registry exchange or information to an
        EIC participant.</Definition> </CodeDescription>
    :cvar B05: <CodeDescription xmlns=""> <Title>EIC code
        publication</Title> <Definition>A document providing EIC
        publication information in a web site publication of a limited
        set of information.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"
    A13 = "A13"
    A14 = "A14"
    A15 = "A15"
    A16 = "A16"
    A17 = "A17"
    A18 = "A18"
    A19 = "A19"
    A20 = "A20"
    A21 = "A21"
    A22 = "A22"
    A23 = "A23"
    A24 = "A24"
    A25 = "A25"
    A26 = "A26"
    A27 = "A27"
    A28 = "A28"
    A30 = "A30"
    A31 = "A31"
    A32 = "A32"
    A33 = "A33"
    A34 = "A34"
    A35 = "A35"
    A36 = "A36"
    A37 = "A37"
    A38 = "A38"
    A39 = "A39"
    A40 = "A40"
    A41 = "A41"
    A42 = "A42"
    A43 = "A43"
    A44 = "A44"
    A45 = "A45"
    A46 = "A46"
    A47 = "A47"
    A48 = "A48"
    A49 = "A49"
    A50 = "A50"
    A51 = "A51"
    A52 = "A52"
    A53 = "A53"
    A54 = "A54"
    A55 = "A55"
    A56 = "A56"
    A57 = "A57"
    A58 = "A58"
    A59 = "A59"
    A60 = "A60"
    A61 = "A61"
    A62 = "A62"
    A63 = "A63"
    A64 = "A64"
    A65 = "A65"
    A66 = "A66"
    A67 = "A67"
    A68 = "A68"
    A69 = "A69"
    A70 = "A70"
    A71 = "A71"
    A72 = "A72"
    A73 = "A73"
    A74 = "A74"
    A75 = "A75"
    A76 = "A76"
    A77 = "A77"
    A78 = "A78"
    A79 = "A79"
    A80 = "A80"
    A81 = "A81"
    A82 = "A82"
    A83 = "A83"
    A84 = "A84"
    A85 = "A85"
    A86 = "A86"
    A87 = "A87"
    A88 = "A88"
    A89 = "A89"
    A90 = "A90"
    A91 = "A91"
    A92 = "A92"
    A93 = "A93"
    A94 = "A94"
    A95 = "A95"
    A96 = "A96"
    A97 = "A97"
    A98 = "A98"
    A99 = "A99"
    B01 = "B01"
    B02 = "B02"
    B03 = "B03"
    B04 = "B04"
    B05 = "B05"


class EicTypeList(Enum):
    """
    :cvar A: <CodeDescription xmlns=""> <Title>Substation</Title>
        <Definition>An EIC code to substations.</Definition>
        </CodeDescription>
    :cvar T: <CodeDescription xmlns=""> <Title>Tieline</Title>
        <Definition>An EIC code to identify tielines.</Definition>
        </CodeDescription>
    :cvar V: <CodeDescription xmlns=""> <Title>Location</Title>
        <Definition>An EIC code to identify locations.</Definition>
        </CodeDescription>
    :cvar W: <CodeDescription xmlns=""> <Title>Resource Object</Title>
        <Definition>An EIC code to identify resource
        objects.</Definition> </CodeDescription>
    :cvar X: <CodeDescription xmlns=""> <Title>Party</Title>
        <Definition>An EIC code to identify parties.</Definition>
        </CodeDescription>
    :cvar Y: <CodeDescription xmlns=""> <Title>Area or Domain</Title>
        <Definition>An EIC code to identify areas or
        domains.</Definition> </CodeDescription>
    :cvar Z: <CodeDescription xmlns=""> <Title>Measurement point</Title>
        <Definition>An EIC code to identify measurement
        points.</Definition> </CodeDescription>
    """

    A = "A"
    T = "T"
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"


class EnergyProductTypeList(Enum):
    """
    :cvar VALUE_8716867000016: <CodeDescription xmlns=""> <Title>Active
        power</Title> <Definition>The product of voltage and the in-
        phase component of alternating current measured in units of
        watts and standard multiples thereof.</Definition>
        </CodeDescription>
    :cvar VALUE_8716867000023: <CodeDescription xmlns="">
        <Title>Reactive power</Title> <Definition>The product of voltage
        and current and the sine of the phase angle between them,
        measured in units of voltamperes reactive and standard multiples
        thereof. (not used for planned schedules).</Definition>
        </CodeDescription>
    :cvar VALUE_8716867000030: <CodeDescription xmlns=""> <Title>Active
        energy</Title> <Definition>The electrical energy produced,
        flowing or supplied by an electrical circuit during a time
        interval, being the integral with respect to time of
        instantaneous active power, measured in units of watt-hours, or
        standard multiples thereof.</Definition> </CodeDescription>
    :cvar VALUE_8716867000047: <CodeDescription xmlns="">
        <Title>Reactive energy</Title> <Definition>The integral with
        respect to time of reactive power (not used for planned
        schedules).</Definition> </CodeDescription>
    :cvar VALUE_8716867000115: <CodeDescription xmlns="">
        <Title>Capacitive reactive power</Title> <Definition>Capacitive
        reactive power.</Definition> </CodeDescription>
    :cvar VALUE_8716867000122: <CodeDescription xmlns="">
        <Title>Inductive reactive power</Title> <Definition>Inductive
        reactive power.</Definition> </CodeDescription>
    :cvar VALUE_8716867000139: <CodeDescription xmlns="">
        <Title>Capacitive Reactive energy</Title> <Definition>Capacitive
        reactive energy.</Definition> </CodeDescription>
    :cvar VALUE_8716867000146: <CodeDescription xmlns="">
        <Title>Inductive Reactive energy</Title> <Definition>Inductive
        reactive energy.</Definition> </CodeDescription>
    :cvar VALUE_8716867009911: <CodeDescription xmlns="">
        <Title>Water</Title> <Definition>For hydro power stations, this
        enables the identification of the quantity of water stored
        behind a dam (volume, head level, etc.), or the constraints in
        the flow of water.</Definition> </CodeDescription>
    """

    VALUE_8716867000016 = "8716867000016"
    VALUE_8716867000023 = "8716867000023"
    VALUE_8716867000030 = "8716867000030"
    VALUE_8716867000047 = "8716867000047"
    VALUE_8716867000115 = "8716867000115"
    VALUE_8716867000122 = "8716867000122"
    VALUE_8716867000139 = "8716867000139"
    VALUE_8716867000146 = "8716867000146"
    VALUE_8716867009911 = "8716867009911"


class FlowCommodityTypeList(Enum):
    """
    :cvar E17: <CodeDescription xmlns=""> <Title>Consumption</Title>
        <Definition> </Definition> </CodeDescription>
    :cvar E18: <CodeDescription xmlns=""> <Title>Production</Title>
        <Definition> </Definition> </CodeDescription>
    :cvar E19: <CodeDescription xmlns=""> <Title>Combined</Title>
        <Definition> </Definition> </CodeDescription>
    """

    E17 = "E17"
    E18 = "E18"
    E19 = "E19"


class FuelTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Unspecified</Title>
        <Definition>Fuel that cannot be associated with any of available
        fuel codes.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Renewable solid
        unspecified</Title> <Definition>Fuel produced in a solid form
        from renewable resources that cannot be associated with any of
        available renewable solid fuel codes.</Definition>
        </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Renewable solid
        municipal waste</Title> <Definition>Solid waste of biological
        material produced by households, hospitals and the tertiary
        sector (in general all waste that resembles household
        waste).</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Renewable solid
        industrial and commercial waste</Title> <Definition>Solid waste
        generated by businesses, production units, bureaus and
        offices.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Renewable solid
        wood</Title> <Definition>Solid wood energy
        resource.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Renewable solid animal
        fats</Title> <Definition>Solid animal fats energy
        resource.</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Renewable solid biomass
        from agriculture</Title> <Definition>Solid by-products and
        residues from agriculture.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Renewable liquid
        unspecified</Title> <Definition>Fuel produced in form of liquid
        from renewable resources that cannot be associated with any of
        available renewable liquid fuel codes.</Definition>
        </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>Renewable liquid
        municipal biodegradable waste</Title> <Definition>Liquid
        municipal waste capable of undergoing anaerobic or aerobic
        decomposition.</Definition> </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Renewable liquid black
        liquor</Title> <Definition>Alkaline-spent liquor obtained from
        the digesters during the production of sulphate or soda
        pulp.</Definition> </CodeDescription>
    :cvar A11: <CodeDescription xmlns=""> <Title>Renewable liquid pure
        plant oil</Title> <Definition>Oil produced from plants, mainly
        from rapeseed and sunflower crops.</Definition>
        </CodeDescription>
    :cvar A12: <CodeDescription xmlns=""> <Title>Renewable liquid waste
        plant oil</Title> <Definition>Oil produced from plants that is
        no longer usable for its originally intended
        purpose.</Definition> </CodeDescription>
    :cvar A13: <CodeDescription xmlns=""> <Title>Renewable liquid
        refined vegetable oil</Title> <Definition>Oil produced from
        plants and transformed into fuel by refining process
        (hydrocracking or hydrogenation).</Definition>
        </CodeDescription>
    :cvar A14: <CodeDescription xmlns=""> <Title>Renewable gaseous
        unspecified</Title> <Definition>Fuel produced in form of gas
        from renewable resources that cannot be associated with any of
        available renewable gaseous fuel codes.</Definition>
        </CodeDescription>
    :cvar A15: <CodeDescription xmlns=""> <Title>Renewable gaseous
        landfill gas</Title> <Definition>Gas produced by digestion of
        land filled waste.</Definition> </CodeDescription>
    :cvar A16: <CodeDescription xmlns=""> <Title>Renewable gaseous
        sewage gas</Title> <Definition>Gas produced from the anaerobic
        fermentation of sewage sludge.</Definition> </CodeDescription>
    :cvar A17: <CodeDescription xmlns=""> <Title>Renewable gaseous
        agricultural gas</Title> <Definition>Gas produced from
        agricultural processes.</Definition> </CodeDescription>
    :cvar A18: <CodeDescription xmlns=""> <Title>Renewable gaseous gas
        from organic waste digestion</Title> <Definition>Gas produced by
        anaerobic digestion process from organic waste.</Definition>
        </CodeDescription>
    :cvar A19: <CodeDescription xmlns=""> <Title>Renewable gaseous
        process gas</Title> <Definition>Gas produced by an industrial
        process as a consequence.</Definition> </CodeDescription>
    :cvar A20: <CodeDescription xmlns=""> <Title>Renewable gaseous other
        biogenic sources</Title> <Definition>Gas produced by form of
        biogenic resource transformation that cannot be associated with
        any of available renewable gaseous fuel codes that use biogenic
        energy resource.</Definition> </CodeDescription>
    :cvar A21: <CodeDescription xmlns=""> <Title>Renewable heating and
        cooling solar</Title> <Definition>Sunlight energy
        source.</Definition> </CodeDescription>
    :cvar A22: <CodeDescription xmlns=""> <Title>Renewable heating and
        cooling geothermal</Title> <Definition>Geothermal energy
        source.</Definition> </CodeDescription>
    :cvar A23: <CodeDescription xmlns=""> <Title>Renewable heating and
        cooling aerothermal</Title> <Definition>Thermal energy obtained
        from air.</Definition> </CodeDescription>
    :cvar A24: <CodeDescription xmlns=""> <Title>Renewable heating and
        cooling hydrothermal</Title> <Definition>Thermal energy obtained
        from large body of water.</Definition> </CodeDescription>
    :cvar A25: <CodeDescription xmlns=""> <Title>Renewable heating and
        cooling process heat</Title> <Definition>Thermal energy obtained
        from process heat.</Definition> </CodeDescription>
    :cvar A26: <CodeDescription xmlns=""> <Title>Renewable mechanical
        unspecified</Title> <Definition>Energy from renewable resource
        transformed into mechanical energy that cannot be associated
        with any of available renewable mechanical fuel
        codes.</Definition> </CodeDescription>
    :cvar A27: <CodeDescription xmlns=""> <Title>Renewable mechanical
        wind</Title> <Definition>Kinetic energy of wind transformed into
        mechanical energy.</Definition> </CodeDescription>
    :cvar A28: <CodeDescription xmlns=""> <Title>Renewable mechanical
        hydro and marine</Title> <Definition>Falling or flowing water
        energy or energy derived from tidal movement, wave motion or
        ocean current.</Definition> </CodeDescription>
    :cvar A29: <CodeDescription xmlns=""> <Title>Fossil
        unspecified</Title> <Definition>Unspecified fossil energy
        source.</Definition> </CodeDescription>
    :cvar A30: <CodeDescription xmlns=""> <Title>Fossil solid
        unspecified</Title> <Definition>Unspecified fossil solid energy
        source.</Definition> </CodeDescription>
    :cvar A31: <CodeDescription xmlns=""> <Title>Fossil solid hard
        coal</Title> <Definition>Hard coal solid fossil energy source.
        This includes Anthracite, Bituminous coal, Coking coal, Coke-
        oven coke and Lignite coke.</Definition> </CodeDescription>
    :cvar A32: <CodeDescription xmlns=""> <Title>Fossil solid brown
        coal</Title> <Definition>Brown coal solid fossil energy source.
        This includes Sub-bituminous coal, Lignite, Brown coal briquette
        and Peat briquette.</Definition> </CodeDescription>
    :cvar A33: <CodeDescription xmlns=""> <Title>Fossil solid
        peat</Title> <Definition>Solid fossil peat energy
        source.</Definition> </CodeDescription>
    :cvar A34: <CodeDescription xmlns=""> <Title>Fossil solid municipal
        waste</Title> <Definition>Solid fossil municipal waste energy
        source.</Definition> </CodeDescription>
    :cvar A35: <CodeDescription xmlns=""> <Title>Fossil solid industrial
        and commercial waste</Title> <Definition>Solid fossil industrial
        and commercial waste energy source.</Definition>
        </CodeDescription>
    :cvar A36: <CodeDescription xmlns=""> <Title>Fossil liquid
        unspecified</Title> <Definition>Unspecified fossil liquid energy
        source.</Definition> </CodeDescription>
    :cvar A37: <CodeDescription xmlns=""> <Title>Fossil liquid crude
        oil</Title> <Definition>Liquid crude oil fossil energy source.
        This includes shale oil or other types.</Definition>
        </CodeDescription>
    :cvar A38: <CodeDescription xmlns=""> <Title>Fossil liquid natural
        gas liquids (NGL)</Title> <Definition>Liquid natural gas liquids
        (NGL) fossil energy source.</Definition> </CodeDescription>
    :cvar A39: <CodeDescription xmlns=""> <Title>Fossil liquid petroleum
        products</Title> <Definition>Liquid petroleum products energy
        source. This includes Ethane,Naphtha, Aviation gasoline , Motor
        gasoline, Aviation turbine fuel,Other kerosene,Gas/diesel oil ,
        Fuel oil, low sulphur ,Fuel oil, high sulphur ,Liquid Petroleum
        Gas , Orimulsion , Bitumen ,Lubricants ,Petroleum coke ,
        Refinery Feedstock.</Definition> </CodeDescription>
    :cvar A40: <CodeDescription xmlns=""> <Title>Fossil gaseous
        unspecified</Title> <Definition>Unspecified fossil gaseous
        energy source.</Definition> </CodeDescription>
    :cvar A41: <CodeDescription xmlns=""> <Title>Fossil gaseous natural
        gas</Title> <Definition>Fossil gaseous natural gas energy
        source.</Definition> </CodeDescription>
    :cvar A42: <CodeDescription xmlns=""> <Title>Fossil gaseous coal-
        derived gas</Title> <Definition>Fossil gaseous coal-derived gas
        energy source. This includes Blast furnace gas,Coke-oven gas or
        other types.</Definition> </CodeDescription>
    :cvar A43: <CodeDescription xmlns=""> <Title>Fossil gaseous
        petroleum products</Title> <Definition>Fossil gaseous petroleum
        products energy  source. This includes Propane, Butane, Refinery
        gas, Chemical waste gas or other types.</Definition>
        </CodeDescription>
    :cvar A44: <CodeDescription xmlns=""> <Title>Fossil gaseous
        municipal gas plant</Title> <Definition>Fossil gaseous municipal
        gas plant energy source. </Definition> </CodeDescription>
    :cvar A45: <CodeDescription xmlns=""> <Title>Fossil gaseous process
        gas</Title> <Definition>Fossil gaseous process gas energy
        source. This includes Carbon monoxide, Methane , Hydrogen
        (fossil sourced) ,Phosphor gas ,Oxy gas and other
        types.</Definition> </CodeDescription>
    :cvar A46: <CodeDescription xmlns=""> <Title>Fossil heat
        unspecified</Title> <Definition>Unspecified fossil heat energy
        source.</Definition> </CodeDescription>
    :cvar A47: <CodeDescription xmlns=""> <Title>Fossil heat process
        heat</Title> <Definition>Fossil process heat energy
        source.</Definition> </CodeDescription>
    :cvar A48: <CodeDescription xmlns=""> <Title>Nuclear solid
        radioactive fuel</Title> <Definition>Solid Nuclear  radioactive
        energy source. This includes UOX, AGR, MOX or other
        types.</Definition> </CodeDescription>
    :cvar A49: <CodeDescription xmlns=""> <Title>Gas synthesis
        unspecified</Title> <Definition>Unspecified gas synthesis energy
        source.</Definition> </CodeDescription>
    :cvar A50: <CodeDescription xmlns=""> <Title>Gas synthesis furnace
        gas</Title> <Definition>Gas synthesis from furnace gas energy
        source.</Definition> </CodeDescription>
    :cvar A51: <CodeDescription xmlns=""> <Title>Waste heat and cold
        unspecified</Title> <Definition>Unspecified Waste heat and cold
        energy source.</Definition> </CodeDescription>
    :cvar A52: <CodeDescription xmlns=""> <Title>Waste heat and cold By-
        product in industrial installation</Title> <Definition>Waste
        heat and cold from by-product in industrial installation energy
        source.</Definition> </CodeDescription>
    :cvar A53: <CodeDescription xmlns=""> <Title>Waste heat and cold By-
        product in power generation</Title> <Definition>Waste heat and
        cold from by-product in power generation energy
        source.</Definition> </CodeDescription>
    :cvar A54: <CodeDescription xmlns=""> <Title>Waste heat and cold By-
        product in tertiary sector</Title> <Definition>Waste heat and
        cold from by-product in tertiary sector energy
        source.</Definition> </CodeDescription>
    :cvar A55: <CodeDescription xmlns=""> <Title>Hydrogen</Title>
        <Definition>Hydrogen energy source.</Definition>
        </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"
    A13 = "A13"
    A14 = "A14"
    A15 = "A15"
    A16 = "A16"
    A17 = "A17"
    A18 = "A18"
    A19 = "A19"
    A20 = "A20"
    A21 = "A21"
    A22 = "A22"
    A23 = "A23"
    A24 = "A24"
    A25 = "A25"
    A26 = "A26"
    A27 = "A27"
    A28 = "A28"
    A29 = "A29"
    A30 = "A30"
    A31 = "A31"
    A32 = "A32"
    A33 = "A33"
    A34 = "A34"
    A35 = "A35"
    A36 = "A36"
    A37 = "A37"
    A38 = "A38"
    A39 = "A39"
    A40 = "A40"
    A41 = "A41"
    A42 = "A42"
    A43 = "A43"
    A44 = "A44"
    A45 = "A45"
    A46 = "A46"
    A47 = "A47"
    A48 = "A48"
    A49 = "A49"
    A50 = "A50"
    A51 = "A51"
    A52 = "A52"
    A53 = "A53"
    A54 = "A54"
    A55 = "A55"


class HvdcmodeTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Setpoint
        schedule</Title> <Definition>The code for the "power setpoint"
        mode of operation of the HVDC link.</Definition>
        </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Proportional external
        signal</Title> <Definition>The code for the "Proportional
        external signal" mode of operation of the HVDC
        link.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>AC emulation</Title>
        <Definition>The code for the "AC emulation" mode of operation of
        the HVDC link.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"


class IndicatorTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>YES</Title>
        <Definition>A positive indication.</Definition>
        </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>NO</Title>
        <Definition>A negative indication.</Definition>
        </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"


class MarketProductTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Standard balancing
        product</Title> <Definition>A harmonised balancing product
        defined by all TSOs for the exchange of balancing
        services.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Specific balancing
        product</Title> <Definition>A product different from a standard
        product.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Product from integrated
        scheduling process</Title> <Definition>From the EBGL Article 2
        (19), means an iterative process that uses at least integrated
        scheduling process bids that contain commercial data, complex
        technical data of individual power generating facilities or
        demand facilities and explicitly includes the start-up
        characteristics, the latest control area adequacy analysis and
        the operational security limits as an input to the
        process.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Local balancing
        product</Title> <Definition>A balancing product that is neither
        standard nor specific. This type may be applicable only in the
        interim period until standard and specific products have been
        defined within the given scheduling area.</Definition>
        </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Standard mFRR product
        eligible for scheduled activation</Title> <Definition>Standard
        mFRR product eligible for scheduled activation.</Definition>
        </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Standard mFRR product
        eligible for direct activation</Title> <Definition>Standard mFRR
        product eligible for direct activation.</Definition>
        </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Standard mFRR product
        eligible for direct and scheduled activation</Title>
        <Definition>Standard mFRR product eligible for direct as well as
        scheduled activation.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Market wide resource
        capacity mechanism</Title> <Definition>This is a market-wide
        resource capacity mechanism where all resource capacity required
        to ensure security of supply receives payment. These mechanisms
        are open for participation to all capacity resources
        contributing to adequacy.</Definition> </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>Strategic reserve
        resource capacity mechanism</Title> <Definition>This is a market
        resource capacity mechanism that is kept outside of the
        electricity market and only used if the market participants do
        not offer enough generation to meet short-term
        demand.</Definition> </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Other resource capacity
        mechanism</Title> <Definition>This is any other kind of market
        resource capacity mechanism.</Definition> </CodeDescription>
    :cvar A11: <CodeDescription xmlns=""> <Title>Fast activation
        product</Title> <Definition>The fast activation product shall be
        considered as a fall-back solution for situations where
        coordination with all parties is no longer possible due to
        insufficient time and the regular product could not be properly
        applied.</Definition> </CodeDescription>
    :cvar A12: <CodeDescription xmlns=""> <Title>Remedial Action Cost
        Sharing Polluter Pays</Title> <Definition>Cost sharing of
        coordinated remedial action measures (redispatch and
        countertrading) under the polluter pays principle.</Definition>
        </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"


class MessageTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Balance responsible
        schedule</Title> <Definition>A schedule which has been prepared
        by a balance responsible party providing planned schedule
        information.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Allocated capacity
        schedule</Title> <Definition>A schedule which has been prepared
        by a capacity allocator providing allocated
        capacity.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Balance area
        schedule</Title> <Definition>A schedule that provides the
        planned schedule information for a balance area.</Definition>
        </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>System Operator area
        schedule</Title> <Definition>A compilation of all external
        schedules concerning two System Operator areas or a connector
        concerning two System Operator of all balance responsible
        parties.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Control block area
        schedule</Title> <Definition>A compilation of all the exchange
        programs of all control areas for one control block with all
        neighbouring control areas of a neighbouring control
        block.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Coordination center
        area schedule</Title> <Definition>A compilation of the exchange
        programs of all exchange blocks divided into UCTE south and
        north.</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Intermediate
        confirmation report</Title> <Definition>An intermediate
        confirmation report that may be produced between final
        cutoffs.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Final confirmation
        report</Title> <Definition>A final confirmation report that is
        produced after a final cutoff.</Definition> </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>Finalised
        schedule</Title> <Definition>A compilation of a set of schedules
        that have been finalized after a given cutoff.</Definition>
        </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Regulation data
        report</Title> <Definition>A compilation of the time series
        employed on a given day to ensure the balance of the
        system.</Definition> </CodeDescription>
    :cvar A11: <CodeDescription xmlns=""> <Title>Aggregated energy data
        report</Title> <Definition>A compilation of the time series of
        all the meter readings or their equivalent for a given
        period.</Definition> </CodeDescription>
    :cvar A12: <CodeDescription xmlns=""> <Title>Imbalance
        report</Title> <Definition>The report containing the complete
        situation of a given period for a party and including the
        schedules, regulation data and actual or calculated
        readings.</Definition> </CodeDescription>
    :cvar A13: <CodeDescription xmlns=""> <Title>Interconnection
        Capacity</Title> <Definition>Document for cross-border capacity
        exchanges.</Definition> </CodeDescription>
    :cvar A14: <CodeDescription xmlns=""> <Title>Resource Provider
        Resource Schedule</Title> <Definition>A document providing the
        schedules for resource objects submitted by a resource
        provider.</Definition> </CodeDescription>
    :cvar A15: <CodeDescription xmlns=""> <Title>Acquiring System
        Operator Reserve Schedule</Title> <Definition>A document
        providing reserve purchases submitted by an Acquiring System
        Operator.</Definition> </CodeDescription>
    :cvar A16: <CodeDescription xmlns=""> <Title>Anomaly Report</Title>
        <Definition>A document providing anomaly information for the
        receiving party to correct.</Definition> </CodeDescription>
    :cvar A17: <CodeDescription xmlns=""> <Title>Acknowledgement
        Document</Title> <Definition>A document providing
        acknowledgement information.</Definition> </CodeDescription>
    :cvar A18: <CodeDescription xmlns=""> <Title>Confirmation
        report</Title> <Definition>A document providing confirmation
        information.</Definition> </CodeDescription>
    :cvar A19: <CodeDescription xmlns=""> <Title>Capacity for
        Resale</Title> <Definition>A document providing information
        about capacity for resale.</Definition> </CodeDescription>
    :cvar A20: <CodeDescription xmlns=""> <Title>Approved Capacity
        Transfer</Title> <Definition>A document to approve a capacity
        transfer.</Definition> </CodeDescription>
    :cvar A21: <CodeDescription xmlns=""> <Title>Capacity transfer
        notification</Title> <Definition>A document notifying a capacity
        transfer.</Definition> </CodeDescription>
    :cvar A22: <CodeDescription xmlns=""> <Title>Transmission rights
        portfolio</Title> <Definition>A document providing the portfolio
        of the transmission capacity rights of a market
        participant.</Definition> </CodeDescription>
    :cvar A23: <CodeDescription xmlns=""> <Title>Allocations</Title>
        <Definition>A document providing the capacity allocations for a
        border.</Definition> </CodeDescription>
    :cvar A24: <CodeDescription xmlns=""> <Title>Bid document</Title>
        <Definition>A document providing bid information.</Definition>
        </CodeDescription>
    :cvar A25: <CodeDescription xmlns=""> <Title>Allocation result
        document</Title> <Definition>A document providing the allocation
        results of an auction.</Definition> </CodeDescription>
    :cvar A26: <CodeDescription xmlns=""> <Title>Capacity
        document</Title> <Definition>A document providing capacity
        information.</Definition> </CodeDescription>
    :cvar A27: <CodeDescription xmlns=""> <Title>Rights document</Title>
        <Definition>A document providing transmission capacity rights
        information.</Definition> </CodeDescription>
    :cvar A28: <CodeDescription xmlns=""> <Title>Generation availability
        schedule</Title> <Definition>This document contains information
        related to energy availability.</Definition> </CodeDescription>
    :cvar A30: <CodeDescription xmlns=""> <Title>Cross border
        schedule</Title> <Definition>This document contains the cross
        border schedules for all the borders of a given country where
        energy is exchanged.</Definition> </CodeDescription>
    :cvar A31: <CodeDescription xmlns=""> <Title>Agreed capacity</Title>
        <Definition>The capacity agreed between parties.</Definition>
        </CodeDescription>
    :cvar A32: <CodeDescription xmlns=""> <Title>Proposed
        capacity</Title> <Definition>The capacity proposed for agreement
        between parties.</Definition> </CodeDescription>
    :cvar A33: <CodeDescription xmlns=""> <Title>System vertical
        load</Title> <Definition>The sum of all flows out of the
        transmission grid via directly connected transformers and lines
        to distribution grids and end consumers as known by the System
        Operator.</Definition> </CodeDescription>
    :cvar A34: <CodeDescription xmlns=""> <Title>Escalation
        document</Title> <Definition>A document which requesting the
        escalation of a situation.</Definition> </CodeDescription>
    :cvar A35: <CodeDescription xmlns=""> <Title>Trouble shooting
        document</Title> <Definition>A document providing trouble
        shooting information for the resolution of a
        problem.</Definition> </CodeDescription>
    :cvar A36: <CodeDescription xmlns=""> <Title>Deactivation
        document</Title> <Definition>A document providing deactivation
        information.</Definition> </CodeDescription>
    :cvar A37: <CodeDescription xmlns=""> <Title>Reserve tender
        document</Title> <Definition>The document that is used for the
        tendering for reserves within the ERRP process.</Definition>
        </CodeDescription>
    :cvar A38: <CodeDescription xmlns=""> <Title>Reserve Allocation
        Result Document</Title> <Definition>The document used to provide
        the results of a Reserve auction.</Definition>
        </CodeDescription>
    :cvar A39: <CodeDescription xmlns=""> <Title>SATCR
        activation</Title> <Definition>The document is used to provide
        the activation of reserves through the SATCR
        process.</Definition> </CodeDescription>
    :cvar A40: <CodeDescription xmlns=""> <Title>DATCR
        activation</Title> <Definition>The document is used to provide
        the activation of reserves through the DATCR
        process.</Definition> </CodeDescription>
    :cvar A41: <CodeDescription xmlns=""> <Title>Activation
        response</Title> <Definition>The document is used to provide a
        response to a request to activate reserves.</Definition>
        </CodeDescription>
    :cvar A42: <CodeDescription xmlns=""> <Title>Tender
        reduction</Title> <Definition>The document is used to provide
        information concerning the reduction of a previously submitted
        tender.</Definition> </CodeDescription>
    :cvar A43: <CodeDescription xmlns=""> <Title>MOL Document</Title>
        <Definition>The document is used to provide Merit Order List
        information.</Definition> </CodeDescription>
    :cvar A44: <CodeDescription xmlns=""> <Title>Price Document</Title>
        <Definition>The document is used to provide market price
        information.</Definition> </CodeDescription>
    :cvar A45: <CodeDescription xmlns=""> <Title>Measurement Value
        Document</Title> <Definition>The document is used to provide
        measurement information from measurement devices.</Definition>
        </CodeDescription>
    :cvar A46: <CodeDescription xmlns=""> <Title>SOAM Document</Title>
        <Definition>The document is used to provide system operator
        accounting data for matching.</Definition> </CodeDescription>
    :cvar A47: <CodeDescription xmlns=""> <Title>SOVA Document</Title>
        <Definition>The document is used to provide system operator
        validated accounting data.</Definition> </CodeDescription>
    :cvar A48: <CodeDescription xmlns=""> <Title>CCVA Document</Title>
        <Definition>The document is used to provide coordination center
        validated accounting data.</Definition> </CodeDescription>
    :cvar A49: <CodeDescription xmlns=""> <Title>Daily settlement
        document</Title> <Definition>The document is used to provide
        daily settlement information.</Definition> </CodeDescription>
    :cvar A50: <CodeDescription xmlns=""> <Title>Weekly settlement
        document</Title> <Definition>The document is used to provide
        weekly settlement information.</Definition> </CodeDescription>
    :cvar A51: <CodeDescription xmlns=""> <Title>Capacity Auction
        Specification Document</Title> <Definition>The document is used
        to provide capacity auction specification
        information.</Definition> </CodeDescription>
    :cvar A52: <CodeDescription xmlns=""> <Title>Market Coupling Results
        Document</Title> <Definition>The document is used to provide the
        results of a market coupling auction.</Definition>
        </CodeDescription>
    :cvar A53: <CodeDescription xmlns=""> <Title>Outage publication
        Document</Title> <Definition>The document is used to provide the
        outage information for publication.</Definition>
        </CodeDescription>
    :cvar A54: <CodeDescription xmlns=""> <Title>Forced generation
        outage Document</Title> <Definition>A document providing
        information on forced generation outages.</Definition>
        </CodeDescription>
    :cvar A55: <CodeDescription xmlns=""> <Title>Summarised Market
        Schedule</Title> <Definition>A compilation of all external
        schedules concerning two Market Balance Areas of all balance
        responsible parties.</Definition> </CodeDescription>
    :cvar A56: <CodeDescription xmlns=""> <Title>Compensation Program
        Schedule</Title> <Definition>A schedule that provides the
        schedule information for the compensation of unintended
        deviation.</Definition> </CodeDescription>
    :cvar A57: <CodeDescription xmlns=""> <Title>Load Frequency Control
        Program Schedule</Title> <Definition>A schedule that provides
        the schedule information for the Load Frequency Control Program
        of a Control Area or a Control Block.</Definition>
        </CodeDescription>
    :cvar A58: <CodeDescription xmlns=""> <Title>Timeframe Independent
        Schedule</Title> <Definition>A compilation of all external
        Timeframe Independent Schedules concerning two System
        Operators.</Definition> </CodeDescription>
    :cvar A59: <CodeDescription xmlns=""> <Title>Information
        request</Title> <Definition>An information request being made
        concerning some specific information.</Definition>
        </CodeDescription>
    :cvar A60: <CodeDescription xmlns=""> <Title>status request for a
        position independently from a specific process</Title>
        <Definition>A status request concerning the position of an
        object independently of any ongoing processes.</Definition>
        </CodeDescription>
    :cvar A61: <CodeDescription xmlns=""> <Title>Estimated Net Transfer
        Capacity</Title> <Definition>The estimated net transfer capacity
        for a given border.</Definition> </CodeDescription>
    :cvar A62: <CodeDescription xmlns=""> <Title>Compensation
        rights</Title> <Definition>The capacity rights that have been
        allocated as compensation.</Definition> </CodeDescription>
    :cvar A63: <CodeDescription xmlns=""> <Title>Redispatch
        notice</Title> <Definition>A notice to confirm the actions
        agreed between System Operators to resolve a congestion
        situation through redispatch.</Definition> </CodeDescription>
    :cvar A64: <CodeDescription xmlns=""> <Title>Tender reduction
        response</Title> <Definition>A response to a tender reduction
        request that provides  corrections to the initial
        document.</Definition> </CodeDescription>
    :cvar A65: <CodeDescription xmlns=""> <Title>System total
        load</Title> <Definition>Total load', including losses without
        power used for energy storage, is equal to generation deducted
        with exports, added with imports and deducted with power used
        for energy storage.</Definition> </CodeDescription>
    :cvar A66: <CodeDescription xmlns=""> <Title>Final MOL</Title>
        <Definition>A document providing the information concerning the
        situation of the MOL at the end of an activation
        period.</Definition> </CodeDescription>
    :cvar A67: <CodeDescription xmlns=""> <Title>Resource Provider
        Schedule for production/consumption</Title> <Definition>A
        document providing the schedules for production/consumption for
        resource objects submitted by a resource provider.</Definition>
        </CodeDescription>
    :cvar A68: <CodeDescription xmlns=""> <Title>Installed generation
        per type</Title> <Definition>A document providing the installed
        generation per generation type.</Definition> </CodeDescription>
    :cvar A69: <CodeDescription xmlns=""> <Title>Wind and solar
        forecast</Title> <Definition>A document providing the forecast
        of wind and solar generation.</Definition> </CodeDescription>
    :cvar A70: <CodeDescription xmlns=""> <Title>Load forecast
        margin</Title> <Definition>A document providing the load
        forecast margin for a period.</Definition> </CodeDescription>
    :cvar A71: <CodeDescription xmlns=""> <Title>Generation
        forecast</Title> <Definition>A document providing the generation
        forecast for a period.</Definition> </CodeDescription>
    :cvar A72: <CodeDescription xmlns=""> <Title>Reservoir filling
        information</Title> <Definition>A document providing information
        concerning the filling of reservoirs.</Definition>
        </CodeDescription>
    :cvar A73: <CodeDescription xmlns=""> <Title>Actual
        generation</Title> <Definition>A document providing the actual
        generation for a period.</Definition> </CodeDescription>
    :cvar A74: <CodeDescription xmlns=""> <Title>Wind and solar
        generation</Title> <Definition>A document providing the
        generation of wind and solar energy for a period.</Definition>
        </CodeDescription>
    :cvar A75: <CodeDescription xmlns=""> <Title>Actual generation per
        type</Title> <Definition>A document providing the actual
        generation per generation type for a period.</Definition>
        </CodeDescription>
    :cvar A76: <CodeDescription xmlns=""> <Title>Load
        unavailability</Title> <Definition>A document providing the
        unavailability of units providing load on the
        network.</Definition> </CodeDescription>
    :cvar A77: <CodeDescription xmlns=""> <Title>Production
        unavailability</Title> <Definition>A document providing the
        unavailability of production units providing energy to the
        network.</Definition> </CodeDescription>
    :cvar A78: <CodeDescription xmlns=""> <Title>Transmission
        unavailability</Title> <Definition>A document providing the
        unavailability of transmission capacity on the
        network.</Definition> </CodeDescription>
    :cvar A79: <CodeDescription xmlns=""> <Title>Offshore grid
        infrastructure unavailability</Title> <Definition>A document
        providing the unavailability of an offshore grid infrastructure
        to the network.</Definition> </CodeDescription>
    :cvar A80: <CodeDescription xmlns=""> <Title>Generation
        unavailability</Title> <Definition>A document providing the
        unavailability of generation units providing energy to the
        network.</Definition> </CodeDescription>
    :cvar A81: <CodeDescription xmlns=""> <Title>Contracted
        reserves</Title> <Definition>A document providing the reserves
        contracted for a period.</Definition> </CodeDescription>
    :cvar A82: <CodeDescription xmlns=""> <Title>Accepted offers</Title>
        <Definition>A document providing the offers of reserves that
        have been accepted for a period.</Definition> </CodeDescription>
    :cvar A83: <CodeDescription xmlns=""> <Title>Activated balancing
        quantities</Title> <Definition>A document providing the
        quantities of reserves that have been activated for
        balancing.</Definition> </CodeDescription>
    :cvar A84: <CodeDescription xmlns=""> <Title>Activated balancing
        prices</Title> <Definition>A document providing the prices of
        the reserves that have been activated for
        balancing.</Definition> </CodeDescription>
    :cvar A85: <CodeDescription xmlns=""> <Title>Imbalance
        prices</Title> <Definition>A document providing the prices of
        reserves due to imbalance for a period.</Definition>
        </CodeDescription>
    :cvar A86: <CodeDescription xmlns=""> <Title>Imbalance
        volume</Title> <Definition>A document providing the volume of
        the imbalance for a period.</Definition> </CodeDescription>
    :cvar A87: <CodeDescription xmlns=""> <Title>Financial
        situation</Title> <Definition>A document providing the financial
        situation for reserves.</Definition> </CodeDescription>
    :cvar A88: <CodeDescription xmlns=""> <Title>Cross border
        balancing</Title> <Definition>A document providing the cross
        border balancing requirements for a period.</Definition>
        </CodeDescription>
    :cvar A89: <CodeDescription xmlns=""> <Title>Contracted reserve
        prices</Title> <Definition>A document providing the price of
        reserves contracted for a period.</Definition>
        </CodeDescription>
    :cvar A90: <CodeDescription xmlns=""> <Title>Interconnection network
        expansion</Title> <Definition>A document providing information
        on the expansion of the interconnection network.</Definition>
        </CodeDescription>
    :cvar A91: <CodeDescription xmlns=""> <Title>Counter trade
        notice</Title> <Definition>A document providing information on
        counter trades for a period.</Definition> </CodeDescription>
    :cvar A92: <CodeDescription xmlns=""> <Title>Congestion
        costs</Title> <Definition>A document providing the cost of
        congestion for a period.</Definition> </CodeDescription>
    :cvar A93: <CodeDescription xmlns=""> <Title>DC link
        capacity</Title> <Definition>A document providing the DC links
        for a period.</Definition> </CodeDescription>
    :cvar A94: <CodeDescription xmlns=""> <Title>Non EU
        allocations</Title> <Definition>A document providing allocations
        made to non EU member states.</Definition> </CodeDescription>
    :cvar A95: <CodeDescription xmlns=""> <Title>Configuration
        document</Title> <Definition>A document providing configuration
        information.</Definition> </CodeDescription>
    :cvar A96: <CodeDescription xmlns=""> <Title>Redispatch activation
        document</Title> <Definition>A document enabling the activation
        of a redispatch notice.</Definition> </CodeDescription>
    :cvar A97: <CodeDescription xmlns=""> <Title>Detailed activation
        history document</Title> <Definition>A document enabling a
        detailed history of activations.</Definition> </CodeDescription>
    :cvar A98: <CodeDescription xmlns=""> <Title>Aggregated activation
        history document</Title> <Definition>A document enabling an
        aggregated history of activations.</Definition>
        </CodeDescription>
    :cvar A99: <CodeDescription xmlns=""> <Title>HVDC Link
        constraints</Title> <Definition>A document providing the
        information concerning the maximum and minimum active power flow
        through each link can limited.</Definition> </CodeDescription>
    :cvar B01: <CodeDescription xmlns=""> <Title>HVDC
        Configuration</Title> <Definition>A document providing the
        information concerning the power set point. The mode in which
        the  HVDC is managed.</Definition> </CodeDescription>
    :cvar B02: <CodeDescription xmlns=""> <Title>HVDC Schedule</Title>
        <Definition>A document providing the information for operating
        DC links.</Definition> </CodeDescription>
    :cvar B03: <CodeDescription xmlns=""> <Title>EIC code
        request</Title> <Definition>A document providing the information
        requesting a new EIC code.</Definition> </CodeDescription>
    :cvar B04: <CodeDescription xmlns=""> <Title>EIC code
        information</Title> <Definition>A document providing EIC
        information  in a central registry exchange or information to an
        EIC participant.</Definition> </CodeDescription>
    :cvar B05: <CodeDescription xmlns=""> <Title>EIC code
        publication</Title> <Definition>A document providing EIC
        publication information in a web site publication of a limited
        set of information.</Definition> </CodeDescription>
    :cvar B06: <CodeDescription xmlns=""> <Title>Critical network
        element determination</Title> <Definition>A document providing
        all the elements necessary for the capacity coordinator to
        determine the transfer capacity and the associated critical
        network elements.</Definition> </CodeDescription>
    :cvar B07: <CodeDescription xmlns=""> <Title>Critical network
        element publication</Title> <Definition>A document providing all
        the elements necessary for the market information aggregator and
        TSOs to know the critical network elements which limit the
        transfer capacity.</Definition> </CodeDescription>
    :cvar B08: <CodeDescription xmlns=""> <Title>Flow based
        domain</Title> <Definition>A document providing the capacity
        domain and its limits available for the TSO.</Definition>
        </CodeDescription>
    :cvar B09: <CodeDescription xmlns=""> <Title>Flow based domain
        publication</Title> <Definition>A document providing the
        capacity domain and its limits available for the
        market.</Definition> </CodeDescription>
    :cvar B10: <CodeDescription xmlns=""> <Title>Flow based domain
        market impact publication</Title> <Definition>A document
        providing the capacity domain and its impacts on the market to
        be published.</Definition> </CodeDescription>
    :cvar B11: <CodeDescription xmlns=""> <Title>Anonymized flow based
        parameters publication</Title> <Definition>A document providing
        all the relevant flow based parameters in case of flow based
        capacity allocation.</Definition> </CodeDescription>
    :cvar B12: <CodeDescription xmlns=""> <Title>Critical network
        element market impact publication</Title> <Definition>A document
        providing the critical network elements and its impacts on the
        market to be published.</Definition> </CodeDescription>
    :cvar B13: <CodeDescription xmlns=""> <Title>Weather
        document</Title> <Definition>An estimation or prediction in
        advance of the weather by analysis of meteorological data and
        the results of what actually happened with the
        weather.</Definition> </CodeDescription>
    :cvar B14: <CodeDescription xmlns=""> <Title>Energy prognosis
        document</Title> <Definition>A document to provide the prognosis
        of energy production/load for a given period.</Definition>
        </CodeDescription>
    :cvar B15: <CodeDescription xmlns=""> <Title>Network constraint
        document</Title> <Definition>A document providing the network
        constraint situations used for the load flow studies. A network
        constraint situation includes contingencies, monitored elements
        and remedial actions.</Definition> </CodeDescription>
    :cvar B16: <CodeDescription xmlns=""> <Title>Aggregated netted
        external market schedule document</Title> <Definition>A document
        used to report aggregated netted external market schedules for a
        given border.</Definition> </CodeDescription>
    :cvar B17: <CodeDescription xmlns=""> <Title>Aggregated netted
        external TSO schedule document</Title> <Definition>A document
        used to report aggregated netted external TSO schedules for a
        given border.</Definition> </CodeDescription>
    :cvar B18: <CodeDescription xmlns=""> <Title>Reporting status market
        document</Title> <Definition>A document used to report the
        status of aggregated netted external market schedules,
        aggregated netted external TSO schedules and compensation
        program schedules on a given border.</Definition>
        </CodeDescription>
    :cvar B19: <CodeDescription xmlns=""> <Title>Reporting information
        market document</Title> <Definition>A document used to report
        the information concerning aggregated netted external schedules,
        aggregated netted external market schedules, aggregated netted
        external TSO schedules, compensation program schedules, netted
        area position schedules and netted area AC position schedules to
        an interested party.</Definition> </CodeDescription>
    :cvar B20: <CodeDescription xmlns=""> <Title>Status request for a
        reporting information market document</Title> <Definition>A
        document requesting the provision of a reporting information
        document.</Definition> </CodeDescription>
    :cvar B21: <CodeDescription xmlns=""> <Title>Reserve need
        document</Title> <Definition>Used by a TSO to send its reserve
        needs.</Definition> </CodeDescription>
    :cvar B22: <CodeDescription xmlns=""> <Title>Generation and load
        shift keys document</Title> <Definition>A document providing the
        values of the generation and load shift keys to be used on
        network model.</Definition> </CodeDescription>
    :cvar B23: <CodeDescription xmlns=""> <Title>Offers to be
        activated</Title> <Definition>A document containing the outcome
        of the process, with the list of offers that are to be activated
        by the TSO concerned and the results for its reserve
        needs.</Definition> </CodeDescription>
    :cvar B24: <CodeDescription xmlns=""> <Title>Clearing price</Title>
        <Definition>A document containing the outcome of the process,
        with the clearing prices for a period.</Definition>
        </CodeDescription>
    :cvar B25: <CodeDescription xmlns=""> <Title>Security analysis
        report</Title> <Definition>A document providing a report on a
        performed security analysis.</Definition> </CodeDescription>
    :cvar B26: <CodeDescription xmlns=""> <Title>Aggregated netted
        external schedule document</Title> <Definition>A document used
        to report aggregated netted external schedules for a given
        border. </Definition> </CodeDescription>
    :cvar B27: <CodeDescription xmlns=""> <Title>External TSO
        schedule</Title> <Definition>A document used to report external
        TSO schedules for a given border or interconnector.</Definition>
        </CodeDescription>
    :cvar B28: <CodeDescription xmlns=""> <Title>Move of scheduled
        production</Title> <Definition>A document indication a move of
        scheduled production.</Definition> </CodeDescription>
    :cvar B29: <CodeDescription xmlns=""> <Title>PS&amp;LC results
        document</Title> <Definition>A document providing Pole Splitting
        &amp;amp; Loss Calculation results.</Definition>
        </CodeDescription>
    :cvar B30: <CodeDescription xmlns=""> <Title>Notification data
        market document</Title> <Definition>A document used to notify
        data to any information receiver.</Definition>
        </CodeDescription>
    :cvar B31: <CodeDescription xmlns=""> <Title>Additional Constraint
        document</Title> <Definition>A document describing additional
        constraints for a capacity calculation process.</Definition>
        </CodeDescription>
    :cvar B32: <CodeDescription xmlns=""> <Title>Operational state
        document</Title> <Definition>A document used for exchanging
        operational states for grid assets.</Definition>
        </CodeDescription>
    :cvar B33: <CodeDescription xmlns=""> <Title>Published offered
        capacity</Title> <Definition>A document providing the most
        recent values of offered capacity.</Definition>
        </CodeDescription>
    :cvar B34: <CodeDescription xmlns=""> <Title>Market result
        document</Title> <Definition>Published prices and
        volumes</Definition> </CodeDescription>
    :cvar B35: <CodeDescription xmlns=""> <Title>Area Configuration
        document</Title> <Definition>A document containing the
        definition of areas.</Definition> </CodeDescription>
    :cvar B36: <CodeDescription xmlns=""> <Title>Area Composition
        document</Title> <Definition>A document containing the relations
        between areas, i.e which Metering Grid Areas a Bidding Zone
        composed of.</Definition> </CodeDescription>
    :cvar B37: <CodeDescription xmlns=""> <Title>Connected Areas
        document</Title> <Definition>A document containing which other
        areas an area is connected to i.e. which Metering Grid Areas a
        Metering Grid Area is connected to.</Definition>
        </CodeDescription>
    :cvar B38: <CodeDescription xmlns=""> <Title>Settlement
        document</Title> <Definition>A document providing settlement
        information.</Definition> </CodeDescription>
    :cvar B39: <CodeDescription xmlns=""> <Title>Imbalance prognosis
        document</Title> <Definition>A document to provide the prognosis
        of energy imbalances for a given period.</Definition>
        </CodeDescription>
    :cvar B40: <CodeDescription xmlns=""> <Title>Complete set of
        bids</Title> <Definition>Submission of complete set of bids. If
        there are existing bids, they should be replaced.</Definition>
        </CodeDescription>
    :cvar B41: <CodeDescription xmlns=""> <Title>Merged MOL
        notice</Title> <Definition>A notice providing information on the
        MOL merging process.</Definition> </CodeDescription>
    :cvar B42: <CodeDescription xmlns=""> <Title>K-factor
        document</Title> <Definition>A document providing K-factor
        values.</Definition> </CodeDescription>
    :cvar B43: <CodeDescription xmlns=""> <Title>Settlement coordination
        document</Title> <Definition>A document providing settlement
        information for coordination between different
        parties.</Definition> </CodeDescription>
    :cvar B44: <CodeDescription xmlns=""> <Title>Financial settlement
        document</Title> <Definition>A document providing financial
        settlement information.</Definition> </CodeDescription>
    :cvar B45: <CodeDescription xmlns=""> <Title>Bid availability
        document</Title> <Definition>A document providing the detailed
        reasons for changing the availability or volume of a
        bid.</Definition> </CodeDescription>
    :cvar B46: <CodeDescription xmlns=""> <Title>Resource capacity unit
        document</Title> <Definition>A document providing information
        about resource capacity units.</Definition> </CodeDescription>
    :cvar B47: <CodeDescription xmlns=""> <Title>Other market
        information</Title> <Definition>A document providing other
        market information.</Definition> </CodeDescription>
    :cvar B48: <CodeDescription xmlns=""> <Title>Permission
        document</Title> <Definition>A document that contains detailed
        information about permissions.</Definition> </CodeDescription>
    :cvar B49: <CodeDescription xmlns=""> <Title>Requested
        capacity</Title> <Definition>A document providing requested
        capacity (e.g. ATC, CZCL) value. </Definition>
        </CodeDescription>
    :cvar B50: <CodeDescription xmlns=""> <Title>Voltage control
        activation document</Title> <Definition>A document providing the
        number of generating units to activate for voltage control, by
        means of their operation in synchronous condenser mode.
        </Definition> </CodeDescription>
    :cvar B51: <CodeDescription xmlns=""> <Title>Transmission inventory
        document</Title> <Definition>A document providing a transmission
        inventory.</Definition> </CodeDescription>
    :cvar B52: <CodeDescription xmlns=""> <Title>Transmission
        inventory</Title> <Definition>A document providing statistics on
        the transmission grid.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"
    A13 = "A13"
    A14 = "A14"
    A15 = "A15"
    A16 = "A16"
    A17 = "A17"
    A18 = "A18"
    A19 = "A19"
    A20 = "A20"
    A21 = "A21"
    A22 = "A22"
    A23 = "A23"
    A24 = "A24"
    A25 = "A25"
    A26 = "A26"
    A27 = "A27"
    A28 = "A28"
    A30 = "A30"
    A31 = "A31"
    A32 = "A32"
    A33 = "A33"
    A34 = "A34"
    A35 = "A35"
    A36 = "A36"
    A37 = "A37"
    A38 = "A38"
    A39 = "A39"
    A40 = "A40"
    A41 = "A41"
    A42 = "A42"
    A43 = "A43"
    A44 = "A44"
    A45 = "A45"
    A46 = "A46"
    A47 = "A47"
    A48 = "A48"
    A49 = "A49"
    A50 = "A50"
    A51 = "A51"
    A52 = "A52"
    A53 = "A53"
    A54 = "A54"
    A55 = "A55"
    A56 = "A56"
    A57 = "A57"
    A58 = "A58"
    A59 = "A59"
    A60 = "A60"
    A61 = "A61"
    A62 = "A62"
    A63 = "A63"
    A64 = "A64"
    A65 = "A65"
    A66 = "A66"
    A67 = "A67"
    A68 = "A68"
    A69 = "A69"
    A70 = "A70"
    A71 = "A71"
    A72 = "A72"
    A73 = "A73"
    A74 = "A74"
    A75 = "A75"
    A76 = "A76"
    A77 = "A77"
    A78 = "A78"
    A79 = "A79"
    A80 = "A80"
    A81 = "A81"
    A82 = "A82"
    A83 = "A83"
    A84 = "A84"
    A85 = "A85"
    A86 = "A86"
    A87 = "A87"
    A88 = "A88"
    A89 = "A89"
    A90 = "A90"
    A91 = "A91"
    A92 = "A92"
    A93 = "A93"
    A94 = "A94"
    A95 = "A95"
    A96 = "A96"
    A97 = "A97"
    A98 = "A98"
    A99 = "A99"
    B01 = "B01"
    B02 = "B02"
    B03 = "B03"
    B04 = "B04"
    B05 = "B05"
    B06 = "B06"
    B07 = "B07"
    B08 = "B08"
    B09 = "B09"
    B10 = "B10"
    B11 = "B11"
    B12 = "B12"
    B13 = "B13"
    B14 = "B14"
    B15 = "B15"
    B16 = "B16"
    B17 = "B17"
    B18 = "B18"
    B19 = "B19"
    B20 = "B20"
    B21 = "B21"
    B22 = "B22"
    B23 = "B23"
    B24 = "B24"
    B25 = "B25"
    B26 = "B26"
    B27 = "B27"
    B28 = "B28"
    B29 = "B29"
    B30 = "B30"
    B31 = "B31"
    B32 = "B32"
    B33 = "B33"
    B34 = "B34"
    B35 = "B35"
    B36 = "B36"
    B37 = "B37"
    B38 = "B38"
    B39 = "B39"
    B40 = "B40"
    B41 = "B41"
    B42 = "B42"
    B43 = "B43"
    B44 = "B44"
    B45 = "B45"
    B46 = "B46"
    B47 = "B47"
    B48 = "B48"
    B49 = "B49"
    B50 = "B50"
    B51 = "B51"
    B52 = "B52"


class ObjectAggregationTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Area</Title>
        <Definition>The object being described concerns an
        area.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Metering point</Title>
        <Definition>The object being described concerns a metering
        point.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Party</Title>
        <Definition>The object being described concerns a
        party.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Agreement
        Identification</Title> <Definition>The object being described
        concerns an agreement identification.</Definition>
        </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Accounting
        point</Title> <Definition>The object being described concerns an
        accounting point.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Resource Object</Title>
        <Definition>The object being described concerns a resource
        object.</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Tieline</Title>
        <Definition>The object being described concerns a
        tieline.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Resource type</Title>
        <Definition>The object being described concerns a resource
        type.</Definition> </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>DC link</Title>
        <Definition>The object being described concerns a DC
        link.</Definition> </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>AC link</Title>
        <Definition>The object being described concerns an AC
        link.</Definition> </CodeDescription>
    :cvar A11: <CodeDescription xmlns=""> <Title>Merchant line</Title>
        <Definition>The object being described concerns a merchant
        line.</Definition> </CodeDescription>
    :cvar A12: <CodeDescription xmlns=""> <Title>Bidding zone</Title>
        <Definition>The largest geographical area within which market
        participants are able to exchange energy without capacity
        allocation.</Definition> </CodeDescription>
    :cvar A13: <CodeDescription xmlns=""> <Title>Virtual bidding
        zone</Title> <Definition>A non-geographical bidding zone to be
        able to apply extra constraints to Bidding Zones.</Definition>
        </CodeDescription>
    :cvar A14: <CodeDescription xmlns=""> <Title>Metering grid
        area</Title> <Definition>A physical area where consumption,
        production and exchange can be measured. It is delimited by the
        placement of meters for continuous measurement for input to, and
        withdrawal from the area.</Definition> </CodeDescription>
    :cvar A15: <CodeDescription xmlns=""> <Title>Scheduling area</Title>
        <Definition>An area within which the TSOs' obligations regarding
        scheduling apply due to operational or organisational
        needs.</Definition> </CodeDescription>
    :cvar A16: <CodeDescription xmlns=""> <Title>Exchange point</Title>
        <Definition>The object being described concerns an exchange
        point.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"
    A13 = "A13"
    A14 = "A14"
    A15 = "A15"
    A16 = "A16"


class PaymentTermsTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Pay as bid</Title>
        <Definition>The amount to be paid shall correspond to the amount
        bid.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Pay as cleared</Title>
        <Definition>The amount to be paid shall correspond to the amount
        calculated for clearing.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>No payment
        terms</Title> <Definition>There are no payment terms to be
        used.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"


class PriceCategoryTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Category 1</Title>
        <Definition>A category one price calculation is to be
        applied.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Category 2</Title>
        <Definition>A category two price calculation is to be
        applied.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Category 3</Title>
        <Definition>A category three price calculation is to be
        applied.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Excess balance</Title>
        <Definition>The category concerns excess balance.</Definition>
        </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Insufficient
        balance</Title> <Definition>A category concerns insufficient
        balance.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Average bid
        price</Title> <Definition>The average bid price for a given
        product.</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Single marginal bid
        price</Title> <Definition>The downwards activated bid price  or
        the upwards activated  bid price for activated balancing
        reserves.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Cross-border marginal
        price</Title> <Definition>The price determined in accordance
        with article 3 of the methodology for pricing balancing
        energy.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"


class PriceComponentTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Scarcity</Title>
        <Definition>A scarcity component to be used in nationally
        defined scarcity situations.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Incentive</Title>
        <Definition>An incentive component to be used to fulfil
        nationally defined boundary conditions.</Definition>
        </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Financial
        neutrality</Title> <Definition>A component related to the
        financial neutrality of the connecting TSO.</Definition>
        </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"


class PriceDirectionTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Expenditure.</Title>
        <Definition>Expenditure, i.e. the Impacted Area System Operator
        pays to the internal Market Parties.</Definition>
        </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Income.</Title>
        <Definition>Income, i.e. The Impacted Area System Operator
        receives from the internal Market Parties.</Definition>
        </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"


class ProcessTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Day ahead</Title>
        <Definition>The information provided concerns a day ahead
        process.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Intra day
        incremental</Title> <Definition>The information provided
        concerns an intra day schedule.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Inter-area
        transit</Title> <Definition>The information provided concerns an
        inter area transit schedule. The rules governing this process
        are market dependent</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>System operation
        closure</Title> <Definition>The information provided concerns
        the closure of a given period of both scheduled and regulation
        information.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Metered data
        aggregation</Title> <Definition>The information provided
        concerns the aggregation process of metered
        information.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Imbalance
        settlement</Title> <Definition>The information provided concerns
        the imbalance settlement for a given period for a balance
        responsible party or parties.</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Capacity
        allocation</Title> <Definition>The information provided concerns
        the capacity allocation process.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Central
        reconciliation</Title> <Definition>The process carried out to
        finalise the imbalance settlement based on actual metered values
        against provisional values from profiled metering points.
        </Definition> </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>Released capacity
        allocation</Title> <Definition>The process concerns the
        notification of capacity rights that are being
        released.</Definition> </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Proposed capacity
        allocation</Title> <Definition>The process concerns the proposed
        capacity to be allocated for a given border.</Definition>
        </CodeDescription>
    :cvar A11: <CodeDescription xmlns=""> <Title>Agreed capacity
        allocation</Title> <Definition>The process concerns the capacity
        that has been agreed for allocation for a border.</Definition>
        </CodeDescription>
    :cvar A12: <CodeDescription xmlns=""> <Title>Long term</Title>
        <Definition>The process concerns scheduling all schedules except
        daily and intraday contracts.</Definition> </CodeDescription>
    :cvar A13: <CodeDescription xmlns=""> <Title>Post scheduling
        adjustment</Title> <Definition>The process concerns the
        adjustments made to previous schedules after the period of
        execution.</Definition> </CodeDescription>
    :cvar A14: <CodeDescription xmlns=""> <Title>Forecast</Title>
        <Definition>The data contained in the document are to be handled
        in short, medium, long term forecasting process.</Definition>
        </CodeDescription>
    :cvar A15: <CodeDescription xmlns=""> <Title>Capacity
        determination</Title> <Definition>The process of determining the
        capacity for use.</Definition> </CodeDescription>
    :cvar A16: <CodeDescription xmlns=""> <Title>Realised</Title>
        <Definition>The process for the treatment of realised data as
        opposed to forecast data.</Definition> </CodeDescription>
    :cvar A17: <CodeDescription xmlns=""> <Title>Schedule day</Title>
        <Definition>The process concerns the day ahead, intraday and
        eventually ex-post scheduling in a single document. The schedule
        will be transferred within the total  position including
        historic information.</Definition> </CodeDescription>
    :cvar A18: <CodeDescription xmlns=""> <Title>Intraday total</Title>
        <Definition>This process concerns an intraday schedule which
        contains the accumulated day ahead and intraday current
        position.</Definition> </CodeDescription>
    :cvar A19: <CodeDescription xmlns=""> <Title>Intraday
        accumulated</Title> <Definition>This process concerns a single
        intraday schedule process where only intraday evolutions occur
        through version changes.</Definition> </CodeDescription>
    :cvar A20: <CodeDescription xmlns=""> <Title>SOMA process</Title>
        <Definition> System Operator meter alignment
        process.</Definition> </CodeDescription>
    :cvar A21: <CodeDescription xmlns=""> <Title>SOVM process</Title>
        <Definition> System Operator validated measurement
        process.</Definition> </CodeDescription>
    :cvar A22: <CodeDescription xmlns=""> <Title>RGCE accounting
        process</Title> <Definition>The document provides ENTSO-E
        Regional Group Continental Europe accounting process
        information.</Definition> </CodeDescription>
    :cvar A23: <CodeDescription xmlns=""> <Title>CCSR RGCE Settlement
        </Title> <Definition>The process concerns the control center
        settlement report for the whole of the ENTSO-E Regional Group
        Continental Europe.</Definition> </CodeDescription>
    :cvar A24: <CodeDescription xmlns=""> <Title>CBSR Settlement
        </Title> <Definition>The process concerns the control block
        settlement report.</Definition> </CodeDescription>
    :cvar A25: <CodeDescription xmlns=""> <Title>CASR Settlement
        </Title> <Definition>The process concerns the control area
        settlement report.</Definition> </CodeDescription>
    :cvar A26: <CodeDescription xmlns=""> <Title>Outage
        information</Title> <Definition>The process concerns TSO
        publication of outages on its power system.</Definition>
        </CodeDescription>
    :cvar A27: <CodeDescription xmlns=""> <Title>Reserve resource
        process</Title> <Definition>The process being described is for
        general reserve resources.</Definition> </CodeDescription>
    :cvar A28: <CodeDescription xmlns=""> <Title>Primary reserve
        process</Title> <Definition>The process being described is for
        primary reserves.</Definition> </CodeDescription>
    :cvar A29: <CodeDescription xmlns=""> <Title>Secondary reserve
        process</Title> <Definition>The process being described is for
        secondary reserves.</Definition> </CodeDescription>
    :cvar A30: <CodeDescription xmlns=""> <Title>Tertiary reserve
        process</Title> <Definition>The process being described is for
        tertiary reserves.</Definition> </CodeDescription>
    :cvar A31: <CodeDescription xmlns=""> <Title>Week ahead</Title>
        <Definition>The process being described is for the week
        ahead.</Definition> </CodeDescription>
    :cvar A32: <CodeDescription xmlns=""> <Title>Month ahead</Title>
        <Definition>The process being described is for the month
        ahead.</Definition> </CodeDescription>
    :cvar A33: <CodeDescription xmlns=""> <Title>Year ahead</Title>
        <Definition>The process being described is for the year
        ahead.</Definition> </CodeDescription>
    :cvar A34: <CodeDescription xmlns=""> <Title>Contracted</Title>
        <Definition>The process being described is for contracted
        information.</Definition> </CodeDescription>
    :cvar A35: <CodeDescription xmlns=""> <Title>Network
        information</Title> <Definition>The process being described is
        for network information.</Definition> </CodeDescription>
    :cvar A36: <CodeDescription xmlns=""> <Title>Creation</Title>
        <Definition>The process being described is for the creation of
        information.</Definition> </CodeDescription>
    :cvar A37: <CodeDescription xmlns=""> <Title>Modification</Title>
        <Definition>The process being described is for the modification
        of information.</Definition> </CodeDescription>
    :cvar A38: <CodeDescription xmlns=""> <Title>Deactivation
        process</Title> <Definition>The process being described is for
        deactivation of information.</Definition> </CodeDescription>
    :cvar A39: <CodeDescription xmlns=""> <Title>Synchronisation
        process</Title> <Definition>The process being described is for
        the synchronisation of information.</Definition>
        </CodeDescription>
    :cvar A40: <CodeDescription xmlns=""> <Title>Intraday
        process</Title> <Definition>The process being described is for
        intraday process.</Definition> </CodeDescription>
    :cvar A41: <CodeDescription xmlns=""> <Title>Redispatch
        process</Title> <Definition>The process being described is for
        redispatch activation.</Definition> </CodeDescription>
    :cvar A42: <CodeDescription xmlns=""> <Title>Activation history
        process</Title> <Definition>The process being described is for
        the provision of an activation history.</Definition>
        </CodeDescription>
    :cvar A43: <CodeDescription xmlns=""> <Title>Flow based domain
        constraint day-ahead</Title> <Definition>The information
        provided concerns the flow-based process in day
        ahead.</Definition> </CodeDescription>
    :cvar A44: <CodeDescription xmlns=""> <Title>Flow based domain
        constraint intraday</Title> <Definition>The information provided
        concerns the flow-based process in intraday.</Definition>
        </CodeDescription>
    :cvar A45: <CodeDescription xmlns=""> <Title>Two days ahead</Title>
        <Definition>Two days ahead.</Definition> </CodeDescription>
    :cvar A46: <CodeDescription xmlns=""> <Title>Replacement
        reserve</Title> <Definition>A process being described is for
        replacement reserves (RR) to restore or support the required
        level of frequency restoration reserves.</Definition>
        </CodeDescription>
    :cvar A47: <CodeDescription xmlns=""> <Title>Manual frequency
        restoration reserve</Title> <Definition>A process being
        described is for manual frequency restoration reserves
        (mFRR).</Definition> </CodeDescription>
    :cvar A48: <CodeDescription xmlns=""> <Title>Day-ahead capacity
        determination</Title> <Definition>The process run at the day-
        ahead timeframe to determine the capacity for use.</Definition>
        </CodeDescription>
    :cvar A49: <CodeDescription xmlns=""> <Title>Intraday capacity
        determination</Title> <Definition>The process run at the
        intraday timeframe to determine the capacity for
        use.</Definition> </CodeDescription>
    :cvar A50: <CodeDescription xmlns=""> <Title>Long term capacity
        determination</Title> <Definition>The process run at the long
        term timeframe to determine the capacity for use.</Definition>
        </CodeDescription>
    :cvar A51: <CodeDescription xmlns=""> <Title>Automatic frequency
        restoration reserve</Title> <Definition>A process being
        described is for automatic frequency restoration reserves
        (aFRR).</Definition> </CodeDescription>
    :cvar A52: <CodeDescription xmlns=""> <Title>Frequency containment
        reserve</Title> <Definition>A process being described is for
        frequency containment reserves (FCR).</Definition>
        </CodeDescription>
    :cvar A53: <CodeDescription xmlns=""> <Title>Common Grid Model (CGM)
        merging process</Title> <Definition>The process for merging
        individual grid models to form the common grid
        model.</Definition> </CodeDescription>
    :cvar A54: <CodeDescription xmlns=""> <Title>Coordinated security
        analysis</Title> <Definition>The process being described is used
        for coordinated security analysis.</Definition>
        </CodeDescription>
    :cvar A55: <CodeDescription xmlns=""> <Title>Exchange of master
        data</Title> <Definition>A process for exchanging master
        data.</Definition> </CodeDescription>
    :cvar A56: <CodeDescription xmlns=""> <Title>Frequency restoration
        reserve</Title> <Definition>The process being described is for
        general frequency restoration reserve.</Definition>
        </CodeDescription>
    :cvar A57: <CodeDescription xmlns=""> <Title>FSKAR
        settlement</Title> <Definition>The information provided concerns
        the Financial Settlement of K?f, ACE and ramping period
        settlement for a given period.</Definition> </CodeDescription>
    :cvar A58: <CodeDescription xmlns=""> <Title>mFRR capacity
        market</Title> <Definition>Processes related to the Reserve
        option market to assure that there are enough available reserves
        for the manual FRR market.</Definition> </CodeDescription>
    :cvar A59: <CodeDescription xmlns=""> <Title>Internal trade
        reporting</Title> <Definition>The process related to internal
        trade reporting.</Definition> </CodeDescription>
    :cvar A60: <CodeDescription xmlns=""> <Title>Scheduled activation
        mFRR</Title> <Definition>mFRR being subject to scheduled
        activation.</Definition> </CodeDescription>
    :cvar A61: <CodeDescription xmlns=""> <Title>Direct activation
        mFRR</Title> <Definition>mFRR being subject to direct
        activation.</Definition> </CodeDescription>
    :cvar A62: <CodeDescription xmlns=""> <Title>Registration</Title>
        <Definition>A process related to the registration and management
        of object information.</Definition> </CodeDescription>
    :cvar A63: <CodeDescription xmlns=""> <Title>Imbalance
        Netting</Title> <Definition>The process described is for
        imbalance netting.</Definition> </CodeDescription>
    :cvar A64: <CodeDescription xmlns=""> <Title>Criteria application
        for instantaneous frequency</Title> <Definition>The  process
        describes criteria application for instantaneous
        frequency.</Definition> </CodeDescription>
    :cvar A65: <CodeDescription xmlns=""> <Title>Criteria application
        for frequency restoration</Title> <Definition>The process
        describes criteria application for frequency
        restoration.</Definition> </CodeDescription>
    :cvar A66: <CodeDescription xmlns=""> <Title>Cost sharing</Title>
        <Definition>The process describes the cost sharing process for
        costly remedial actions.</Definition> </CodeDescription>
    :cvar A67: <CodeDescription xmlns=""> <Title>Central selection
        aFRR</Title> <Definition>aFRR subject to central selection of
        bids for activation.</Definition> </CodeDescription>
    :cvar A68: <CodeDescription xmlns=""> <Title>Local selection
        aFRR</Title> <Definition>aFRR subject to local selection of bids
        for activation.</Definition> </CodeDescription>
    :cvar A69: <CodeDescription xmlns=""> <Title>Common grid model
        alignment</Title> <Definition>The process for aligning bidding
        zone net positions.</Definition> </CodeDescription>
    :cvar A70: <CodeDescription xmlns=""> <Title>Pan-European
        verification function</Title> <Definition>The process for
        verifying bidding zone net positions.</Definition>
        </CodeDescription>
    :cvar A71: <CodeDescription xmlns=""> <Title>Outage planning
        coordination</Title> <Definition>The process being described is
        used for outage planning coordination.</Definition>
        </CodeDescription>
    :cvar A72: <CodeDescription xmlns=""> <Title>Short term
        adequacy</Title> <Definition>The process being described is used
        for short term adequacy calculations.</Definition>
        </CodeDescription>
    :cvar A73: <CodeDescription xmlns=""> <Title>Coordinated capacity
        calculation</Title> <Definition>The process being described is
        used for coordinated capacity calculation.</Definition>
        </CodeDescription>
    :cvar A74: <CodeDescription xmlns=""> <Title>Access to metered
        data</Title> <Definition>Access to meter readings of electricity
        consumption from or electricity feed into the grid.</Definition>
        </CodeDescription>
    :cvar A75: <CodeDescription xmlns=""> <Title>Permission
        administration</Title> <Definition>Administration of permissions
        to access and/or use data.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"
    A13 = "A13"
    A14 = "A14"
    A15 = "A15"
    A16 = "A16"
    A17 = "A17"
    A18 = "A18"
    A19 = "A19"
    A20 = "A20"
    A21 = "A21"
    A22 = "A22"
    A23 = "A23"
    A24 = "A24"
    A25 = "A25"
    A26 = "A26"
    A27 = "A27"
    A28 = "A28"
    A29 = "A29"
    A30 = "A30"
    A31 = "A31"
    A32 = "A32"
    A33 = "A33"
    A34 = "A34"
    A35 = "A35"
    A36 = "A36"
    A37 = "A37"
    A38 = "A38"
    A39 = "A39"
    A40 = "A40"
    A41 = "A41"
    A42 = "A42"
    A43 = "A43"
    A44 = "A44"
    A45 = "A45"
    A46 = "A46"
    A47 = "A47"
    A48 = "A48"
    A49 = "A49"
    A50 = "A50"
    A51 = "A51"
    A52 = "A52"
    A53 = "A53"
    A54 = "A54"
    A55 = "A55"
    A56 = "A56"
    A57 = "A57"
    A58 = "A58"
    A59 = "A59"
    A60 = "A60"
    A61 = "A61"
    A62 = "A62"
    A63 = "A63"
    A64 = "A64"
    A65 = "A65"
    A66 = "A66"
    A67 = "A67"
    A68 = "A68"
    A69 = "A69"
    A70 = "A70"
    A71 = "A71"
    A72 = "A72"
    A73 = "A73"
    A74 = "A74"
    A75 = "A75"


class QualityTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Adjusted</Title>
        <Definition>The contents of the object have been
        adjusted.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Not available</Title>
        <Definition>The contents of the object are not
        available.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Estimated</Title>
        <Definition>The contents of the object are estimated. The code
        is typically used when measured values are missing and an
        estimate is made based on historical data. </Definition>
        </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>As provided</Title>
        <Definition>The contents of the object are as
        provided.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Incomplete</Title>
        <Definition>The contents of the object are calculated based on
        incomplete data.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Calculated</Title>
        <Definition>The contents of the object are calculated. The code
        is typically used when a value is calculated based on several
        other known values.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"


class ReasonCodeTypeList(Enum):
    """
    :cvar VALUE_999: <CodeDescription xmlns=""> <Title>Errors not
        specifically identified </Title> <Definition>This code is used
        to identify errors that have not been specifically addressed in
        the Reason code list. It can be used at any level and refers to
        the level for which it has been identified.</Definition>
        </CodeDescription>
    :cvar A01: <CodeDescription xmlns=""> <Title>Message fully
        accepted</Title> <Definition>The message has been fully accepted
        for application processing.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Message fully rejected
        </Title> <Definition>No part of the message has been accepted
        for application processing, e.g. Global position
        incomplete.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Message contains errors
        at the time series level </Title> <Definition>Part of the
        message contents, i.e. certain time series, has been accepted
        for application processing. It is necessary to look at the time
        series level to determine the time series that have been
        rejected. The time series is excluded from the global
        position.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Time interval incorrect
        </Title> <Definition>The schedule time interval is not within
        the contractual agreement or the period does not agree with the
        schedule time interval.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Sender without valid
        contract </Title> <Definition>The sender has no current valid
        contract with the TSO. The message consequently will be fully
        rejected.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Schedule accepted
        </Title> <Definition>The schedule of the recipient as presented
        has been completely accepted.</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Schedule partially
        accepted </Title> <Definition>The schedule of the recipient as
        presented has been partially accepted. It is necessary to look
        at the time series level to determine the changes (time series
        rejected, modified, etc.).</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Schedule rejected
        </Title> <Definition>The schedule of the recipient as presented
        has been totally rejected. The cause could be the non
        presentation of a counter part for the involved
        trades.</Definition> </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>Time series not
        matching</Title> <Definition>Time series mismatches.
        </Definition> </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Credit limit exceeded
        </Title> <Definition>The contractual credit limit has been
        exceeded and as such the message has been rejected.</Definition>
        </CodeDescription>
    :cvar A20: <CodeDescription xmlns=""> <Title>Time series fully
        rejected </Title> <Definition>The time series has been fully
        rejected. In the case of a confirmation report, this reason code
        is used in conjunction with either A26 or A30.</Definition>
        </CodeDescription>
    :cvar A21: <CodeDescription xmlns=""> <Title>Time series accepted
        with specific time interval errors </Title> <Definition>The time
        series has been accepted but some time interval quantities have
        been rectified or zeroed out.</Definition> </CodeDescription>
    :cvar A22: <CodeDescription xmlns=""> <Title>In party/Out party
        invalid</Title> <Definition>There is no contract for the parties
        indicated or the rules for cross border nominations are not
        being respected. The time series has been rejected.</Definition>
        </CodeDescription>
    :cvar A23: <CodeDescription xmlns=""> <Title>Area invalid</Title>
        <Definition>The area is unknown or not allowed. The time series
        has been rejected.</Definition> </CodeDescription>
    :cvar A24: <CodeDescription xmlns=""> <Title>A24 not
        applicable</Title> <Definition>This code is no longer
        applicable.</Definition> </CodeDescription>
    :cvar A25: <CodeDescription xmlns=""> <Title>A25 not
        applicable</Title> <Definition>This code is no longer
        applicable.</Definition> </CodeDescription>
    :cvar A26: <CodeDescription xmlns=""> <Title>Default time series
        applied </Title> <Definition>The time series has been rejected
        and replaced with a default time series profile. This reason
        code may not be used in conjunction with A30.</Definition>
        </CodeDescription>
    :cvar A27: <CodeDescription xmlns=""> <Title>Cross border capacity
        exceeded </Title> <Definition>The cross border capacity has been
        exceeded. The time series has been rejected or
        adjusted.</Definition> </CodeDescription>
    :cvar A28: <CodeDescription xmlns=""> <Title>Counterpart time series
        missing </Title> <Definition>This provides an indication that
        the time series has not got a counterpart time series. In the
        case of an Intermediate Confirmation Report this is advising the
        recipient that the time series may be rejected at nomination
        closure if the counterpart time series is not received. In the
        case of a Final Confirmation Report this is informing the
        recipient that the time series has been rejected because the
        counterpart time series has not been forthcoming. </Definition>
        </CodeDescription>
    :cvar A29: <CodeDescription xmlns=""> <Title>Counterpart time series
        quantity differences </Title> <Definition>The time series has
        been rejected as it does not match that of the counterpart who
        is considered by market rules to be correct.</Definition>
        </CodeDescription>
    :cvar A30: <CodeDescription xmlns=""> <Title>Imposed Time series
        from nominated party's time series (party identified in reason
        text)</Title> <Definition>The nominated party's time series has
        replaced the current time series. This reason code may not be
        used in conjunction with A26.</Definition> </CodeDescription>
    :cvar A41: <CodeDescription xmlns=""> <Title>Resolution
        inconsistency </Title> <Definition>The resolution is not
        coherent with the time interval, or resolution not
        valid.</Definition> </CodeDescription>
    :cvar A42: <CodeDescription xmlns=""> <Title>Quantity inconsistency
        </Title> <Definition>The quantity is not coherent. For example a
        time period with the same version number but different
        quantities or an non permitted number of digits after the
        decimal point, etc.</Definition> </CodeDescription>
    :cvar A43: <CodeDescription xmlns=""> <Title>Quantity increased
        </Title> <Definition>The quantity has been increased in order to
        satisfy minimum constraints.</Definition> </CodeDescription>
    :cvar A44: <CodeDescription xmlns=""> <Title>Quantity decreased
        </Title> <Definition>The quantity has been decreased in order to
        satisfy congestion constraints.</Definition> </CodeDescription>
    :cvar A45: <CodeDescription xmlns=""> <Title>Default quantity
        applied </Title> <Definition>The default quantity has been
        applied as the current quantity does not satisfy contractual
        obligations.</Definition> </CodeDescription>
    :cvar A46: <CodeDescription xmlns=""> <Title>Quantities must not be
        signed values</Title> <Definition>The quantity proposed is
        illegal since signed values are only permitted in specific
        circumstances.</Definition> </CodeDescription>
    :cvar A47: <CodeDescription xmlns=""> <Title>A47 not
        applicable</Title> <Definition>This code is no longer
        applicable.</Definition> </CodeDescription>
    :cvar A48: <CodeDescription xmlns=""> <Title>Modification
        reason</Title> <Definition>In an intraday transmission, the
        reason for the modification is as follows (in the reason
        text).</Definition> </CodeDescription>
    :cvar A49: <CodeDescription xmlns=""> <Title>Position
        inconsistency</Title> <Definition>A position is missing or too
        many.</Definition> </CodeDescription>
    :cvar A50: <CodeDescription xmlns=""> <Title>Senders time series
        version conflict</Title> <Definition>There is an error in the
        sender time series version, i.e. it could be superior to the
        message version or is inconsistent with the existing data. The
        time series has been rejected.</Definition> </CodeDescription>
    :cvar A51: <CodeDescription xmlns=""> <Title>Message identification
        or version conflict</Title> <Definition>The message
        identification is already in the receiving system. Or a higher
        version already exists. Message rejected.</Definition>
        </CodeDescription>
    :cvar A52: <CodeDescription xmlns=""> <Title>Time series missing
        from new version of message</Title> <Definition>A time series is
        not contained in a new version of the message. Message
        rejected.</Definition> </CodeDescription>
    :cvar A53: <CodeDescription xmlns=""> <Title>Receiving party
        incorrect</Title> <Definition>The receiving party is incorrect.
        Message rejected.</Definition> </CodeDescription>
    :cvar A54: <CodeDescription xmlns=""> <Title>Global position not in
        balance</Title> <Definition>The message does not balance out to
        zero. Market rules might require that the message is rejected.
        </Definition> </CodeDescription>
    :cvar A55: <CodeDescription xmlns=""> <Title>Time series
        identification conflict</Title> <Definition>The identification
        of the time series is duplicated or incorrect. Time series will
        be rejected.</Definition> </CodeDescription>
    :cvar A56: <CodeDescription xmlns=""> <Title>Corresponding Time
        series not netted</Title> <Definition>All corresponding time
        series must be netted. Time series rejected.</Definition>
        </CodeDescription>
    :cvar A57: <CodeDescription xmlns=""> <Title>Deadline limit
        exceeded/Gate not open</Title> <Definition>The deadline for
        receiving schedule messages has passed. Message or time series
        rejected.</Definition> </CodeDescription>
    :cvar A58: <CodeDescription xmlns=""> <Title>One to one nomination
        inconsistency</Title> <Definition>There is a one to one
        nomination inconstancy with the in/out parties or areas. Time
        series rejected.</Definition> </CodeDescription>
    :cvar A59: <CodeDescription xmlns=""> <Title>Not compliant to local
        market rules</Title> <Definition>The level in which this is
        identified is not in compliance with local market rules. The
        level in question has been rejected.</Definition>
        </CodeDescription>
    :cvar A60: <CodeDescription xmlns=""> <Title>Inter-area transit
        schedule exceeds nominated schedule</Title> <Definition>The
        inter-area transit schedule exceeds the nominated schedule for
        the same time interval. The inter-area transit schedule is
        rejected.</Definition> </CodeDescription>
    :cvar A61: <CodeDescription xmlns=""> <Title>Currency
        invalid</Title> <Definition>The currency is not in compliance
        with ISO 4217.</Definition> </CodeDescription>
    :cvar A62: <CodeDescription xmlns=""> <Title>Invalid business
        type</Title> <Definition>The business type does not belong to
        the valid set of business types for the process in
        question.</Definition> </CodeDescription>
    :cvar A63: <CodeDescription xmlns=""> <Title>Time Series
        modified</Title> <Definition>The time series has been
        modified.</Definition> </CodeDescription>
    :cvar A64: <CodeDescription xmlns=""> <Title>Resource Object
        Invalid</Title> <Definition>The Resource Object defined in the
        document is not valid.</Definition> </CodeDescription>
    :cvar A65: <CodeDescription xmlns=""> <Title>Reserve object
        Technical  limits exceeded</Title> <Definition>Reserve objects
        aggregated values are not within technical/prequalified
        limits</Definition> </CodeDescription>
    :cvar A66: <CodeDescription xmlns=""> <Title>Planned reserves do not
        correspond with contractual data</Title> <Definition>Planned
        reserves do not correspond with contractual data.</Definition>
        </CodeDescription>
    :cvar A67: <CodeDescription xmlns=""> <Title>Limit Data is not
        available</Title> <Definition>Limit Data is not
        available.</Definition> </CodeDescription>
    :cvar A68: <CodeDescription xmlns=""> <Title>Reserve Object not
        qualified for reserve type</Title> <Definition>Reserve Object is
        not qualified for reserve type.</Definition> </CodeDescription>
    :cvar A69: <CodeDescription xmlns=""> <Title>Mandatory attributes
        missing</Title> <Definition>Mandatory attributes
        missing.</Definition> </CodeDescription>
    :cvar A70: <CodeDescription xmlns=""> <Title>Curtailment</Title>
        <Definition>The capacity in question has been
        curtailed.</Definition> </CodeDescription>
    :cvar A71: <CodeDescription xmlns=""> <Title>Linked bid rejected due
        to associated bid unsuccessful</Title> <Definition>The bid in
        question has been rejected because an associated bid has been
        unsuccessful.</Definition> </CodeDescription>
    :cvar A72: <CodeDescription xmlns=""> <Title>Original bid divided to
        permit acceptance</Title> <Definition>The original bid quantity
        has been divided to enable it to be accepted.</Definition>
        </CodeDescription>
    :cvar A73: <CodeDescription xmlns=""> <Title>Bid accepted</Title>
        <Definition>The bid in question has been accepted.</Definition>
        </CodeDescription>
    :cvar A74: <CodeDescription xmlns=""> <Title>Auction Status</Title>
        <Definition>The information in the Reason Text provides auction
        status information.</Definition> </CodeDescription>
    :cvar A75: <CodeDescription xmlns=""> <Title>Right status
        information</Title> <Definition>The information in the Reason
        Text provides status information concerning the transmission
        rights in question.</Definition> </CodeDescription>
    :cvar A76: <CodeDescription xmlns=""> <Title>Agreement
        identification inconsistency</Title> <Definition>There is an
        inconsistency between the contract type and the agreement
        identification.</Definition> </CodeDescription>
    :cvar A77: <CodeDescription xmlns=""> <Title>Dependency matrix not
        respected</Title> <Definition>There is an inconsistency between
        the document contents and the dependency matrix.</Definition>
        </CodeDescription>
    :cvar A78: <CodeDescription xmlns=""> <Title>Sender identification
        and/or role invalid</Title> <Definition>The identification of
        the sender or the sender/role combination is
        invalid.</Definition> </CodeDescription>
    :cvar A79: <CodeDescription xmlns=""> <Title>Process type
        invalid</Title> <Definition>The process type does not figure in
        the list of valid process types for this document.</Definition>
        </CodeDescription>
    :cvar A80: <CodeDescription xmlns=""> <Title>Domain invalid</Title>
        <Definition>The domain does not figure in the list of valid
        domains for this document and process.</Definition>
        </CodeDescription>
    :cvar A81: <CodeDescription xmlns=""> <Title>Matching period
        invalid</Title> <Definition>The period is not within the
        expected limits.</Definition> </CodeDescription>
    :cvar A82: <CodeDescription xmlns=""> <Title>In/Out area
        inconsistent with domain</Title> <Definition>The in and out area
        does not figure within the domain specified.</Definition>
        </CodeDescription>
    :cvar A83: <CodeDescription xmlns=""> <Title>Disagree with matching
        results</Title> <Definition>The matching results provided are
        not consistent.</Definition> </CodeDescription>
    :cvar A84: <CodeDescription xmlns=""> <Title>Confirmation ignored
        due to higher version already received</Title> <Definition>The
        report has been ignored since a higher version has been
        received.</Definition> </CodeDescription>
    :cvar A85: <CodeDescription xmlns=""> <Title>Confirmation without
        adjustment (time series have been matched without
        change)</Title> <Definition>The report has been successfully
        matched without any changes.</Definition> </CodeDescription>
    :cvar A86: <CodeDescription xmlns=""> <Title>Confirmation with
        adjustment (time series have been modified)</Title>
        <Definition>The report has been matched but required
        adjustment.</Definition> </CodeDescription>
    :cvar A87: <CodeDescription xmlns=""> <Title>For action (only in
        intermediate confirmation - time series need mutual agreement
        and action)</Title> <Definition>The report in question is only
        for action in an intermediate stage.</Definition>
        </CodeDescription>
    :cvar A88: <CodeDescription xmlns=""> <Title>Time series
        matched</Title> <Definition>The time series has been
        successfully matched.</Definition> </CodeDescription>
    :cvar A89: <CodeDescription xmlns=""> <Title>Time series ignored
        (note: this can only apply to time series that are set to zero -
        see matching principles)</Title> <Definition>The time series has
        been ignored and not matched since it does not figure in a
        counterparty transmission. All are correctly equal to
        zero.</Definition> </CodeDescription>
    :cvar A90: <CodeDescription xmlns=""> <Title>Modification proposal
        (intermediate confirmation)</Title> <Definition>The document is
        a proposal for change before finalization.</Definition>
        </CodeDescription>
    :cvar A91: <CodeDescription xmlns=""> <Title>Expected document not
        received</Title> <Definition>The document that is expected has
        not been received within the expected timeframe.</Definition>
        </CodeDescription>
    :cvar A92: <CodeDescription xmlns=""> <Title>Not possible to send
        document on time, but estimated delivery time is
        provided</Title> <Definition>The document that is due cannot be
        transmitted within the required timeframe. An estimated time of
        transmission is provided.</Definition> </CodeDescription>
    :cvar A93: <CodeDescription xmlns=""> <Title>Not possible to send
        document on time, and furthermore no expected time of return to
        normal situation</Title> <Definition>The document that is due
        cannot be transmitted within the required timeframe. The time of
        transmission of the document is unknown.</Definition>
        </CodeDescription>
    :cvar A94: <CodeDescription xmlns=""> <Title>Document cannot be
        processed by receiving system</Title> <Definition>The receiving
        system cannot process that document in question.</Definition>
        </CodeDescription>
    :cvar A95: <CodeDescription xmlns=""> <Title>Complementary
        information</Title> <Definition>Additional text is provided in
        order to further explain a condition, for example to provide
        details of an outage.</Definition> </CodeDescription>
    :cvar A96: <CodeDescription xmlns=""> <Title>Technical
        constraint</Title> <Definition>A technical constraint has been
        applied.</Definition> </CodeDescription>
    :cvar A97: <CodeDescription xmlns=""> <Title>Force majeure
        curtailment</Title> <Definition>Curtailment due to Force
        Majeure. A code that enables the identification of the
        curtailment reason for settlement purposes.</Definition>
        </CodeDescription>
    :cvar A98: <CodeDescription xmlns=""> <Title>Network security
        curtailment</Title> <Definition>Curtailment due to network
        security reasons A code that enables the identification of the
        curtailment reason for settlement purposes.</Definition>
        </CodeDescription>
    :cvar A99: <CodeDescription xmlns=""> <Title>Auction
        cancelled</Title> <Definition>The auction has been
        cancelled.</Definition> </CodeDescription>
    :cvar B01: <CodeDescription xmlns=""> <Title>Incomplete
        document</Title> <Definition>The document is incomplete and
        cannot be processed.</Definition> </CodeDescription>
    :cvar B02: <CodeDescription xmlns=""> <Title>Accounting Point (tie-
        line) Time Series missing</Title> <Definition>The document is
        incomplete as a time series for an accounting point is
        missing.</Definition> </CodeDescription>
    :cvar B03: <CodeDescription xmlns=""> <Title>Meter data Time series
        missing</Title> <Definition>The document is incomplete as a time
        series for meter data is missing.</Definition>
        </CodeDescription>
    :cvar B04: <CodeDescription xmlns=""> <Title>Estimated values not
        allowed in first transmission</Title> <Definition>The document
        is in its initial form and estimated values are not
        allowed.</Definition> </CodeDescription>
    :cvar B05: <CodeDescription xmlns=""> <Title>No quantity values
        allowed for a quality that is not available</Title>
        <Definition>No quantity values are allowed for a quality that is
        not available.</Definition> </CodeDescription>
    :cvar B06: <CodeDescription xmlns=""> <Title>Time series
        accepted</Title> <Definition>Time series accepted.</Definition>
        </CodeDescription>
    :cvar B07: <CodeDescription xmlns=""> <Title>Auction without bids
        being entered</Title> <Definition>The auction has terminated
        without any bids being submitted. The ReasonText may provide the
        identification of the auction in question.</Definition>
        </CodeDescription>
    :cvar B08: <CodeDescription xmlns=""> <Title>Data not yet
        available</Title> <Definition>It is not possible to perform the
        necessary action since the required data for this action is not
        yet available.</Definition> </CodeDescription>
    :cvar B09: <CodeDescription xmlns=""> <Title>Bid not
        accepted</Title> <Definition>The bid in question has not been
        accepted.</Definition> </CodeDescription>
    :cvar B10: <CodeDescription xmlns=""> <Title>Initiator area
        problem</Title> <Definition>The problem concerns the initiator
        area.</Definition> </CodeDescription>
    :cvar B11: <CodeDescription xmlns=""> <Title>Cooperating area
        problem</Title> <Definition>The problem concerns the cooperating
        area.</Definition> </CodeDescription>
    :cvar B12: <CodeDescription xmlns=""> <Title>Communication status
        currently active</Title> <Definition>The status within the
        system indicates that the communication capability is currently
        active.</Definition> </CodeDescription>
    :cvar B13: <CodeDescription xmlns=""> <Title>Communication status
        currently inactive</Title> <Definition>The status within the
        system indicates that the communication capability is currently
        inactive.</Definition> </CodeDescription>
    :cvar B14: <CodeDescription xmlns=""> <Title>Communication status
        currently restricted</Title> <Definition>The status within the
        system indicates that the communication capability is currently
        restricted.</Definition> </CodeDescription>
    :cvar B15: <CodeDescription xmlns=""> <Title>Problem associated with
        both areas</Title> <Definition>The problem concerns both
        areas.</Definition> </CodeDescription>
    :cvar B16: <CodeDescription xmlns=""> <Title>Tender unavailable in
        MOL list</Title> <Definition>A tender that has been requested is
        no longer available in the MOL.</Definition> </CodeDescription>
    :cvar B17: <CodeDescription xmlns=""> <Title>Price based on
        preliminary exchange rate</Title> <Definition>The price is based
        on a preliminary exchange rate.</Definition> </CodeDescription>
    :cvar B18: <CodeDescription xmlns=""> <Title>Failure</Title>
        <Definition>A failure has occurred.</Definition>
        </CodeDescription>
    :cvar B19: <CodeDescription xmlns=""> <Title>Foreseen
        maintenance</Title> <Definition>Maintenance is
        foreseen.</Definition> </CodeDescription>
    :cvar B20: <CodeDescription xmlns=""> <Title>Shutdown</Title>
        <Definition>A shutdown has occurred.</Definition>
        </CodeDescription>
    :cvar B21: <CodeDescription xmlns=""> <Title>Official exchange rate
        approved</Title> <Definition>The official exchange rate has been
        approved.</Definition> </CodeDescription>
    :cvar B22: <CodeDescription xmlns=""> <Title>System
        regulation</Title> <Definition>The information provided regards
        a regulation for system purposes.</Definition>
        </CodeDescription>
    :cvar B23: <CodeDescription xmlns=""> <Title>Frequency
        regulation</Title> <Definition>The information provided regards
        a regulation for frequency purposes.</Definition>
        </CodeDescription>
    :cvar B24: <CodeDescription xmlns=""> <Title>Load flow
        overload</Title> <Definition>Situation in the grid, where
        loading of a certain grid element, e.g. overhead line, is above
        defined technical limits.</Definition> </CodeDescription>
    :cvar B25: <CodeDescription xmlns=""> <Title>Voltage level
        adjustment</Title> <Definition>A TSO activity to maintain an
        acceptable voltage profile throughout the network. This is
        achieved by balancing of the respective reactive power
        requirements of the network and the customers.</Definition>
        </CodeDescription>
    :cvar B26: <CodeDescription xmlns=""> <Title>Emergency situation
        curtailment</Title> <Definition>Curtailment due to emergency
        situation. A code that enables the identification of the
        curtailment reason for settlement purposes.</Definition>
        </CodeDescription>
    :cvar B27: <CodeDescription xmlns=""> <Title>Calculation process
        failed</Title> <Definition>The calculation has not been
        performed.</Definition> </CodeDescription>
    :cvar B28: <CodeDescription xmlns=""> <Title>No capacity constraint
        impact on the market</Title> <Definition>The market position is
        such as no capacity constraint is applied to limit the cross
        border exchanges.</Definition> </CodeDescription>
    :cvar B29: <CodeDescription xmlns=""> <Title>Special
        Condition</Title> <Definition>Special condition need to be
        fulfilled.</Definition> </CodeDescription>
    :cvar B30: <CodeDescription xmlns=""> <Title>Unverified</Title>
        <Definition>Missing or not validated data.</Definition>
        </CodeDescription>
    :cvar B31: <CodeDescription xmlns=""> <Title>Verified</Title>
        <Definition>Data has successfully passed the verification
        process.</Definition> </CodeDescription>
    :cvar B32: <CodeDescription xmlns=""> <Title>CGM
        inconsistency</Title> <Definition>Describes an element which was
        not found in the CGM.</Definition> </CodeDescription>
    :cvar B33: <CodeDescription xmlns=""> <Title>Network dictionary
        inconsistency</Title> <Definition>Describes an element which was
        not found in the network dictionary.</Definition>
        </CodeDescription>
    :cvar B34: <CodeDescription xmlns=""> <Title>Capacity reduced by
        TSO</Title> <Definition>Describes a capacity that was reduced by
        a TSO.</Definition> </CodeDescription>
    :cvar B35: <CodeDescription xmlns=""> <Title>Overload</Title>
        <Definition>Describes an N-k or N state overload.</Definition>
        </CodeDescription>
    :cvar B36: <CodeDescription xmlns=""> <Title>GLSK limitation</Title>
        <Definition>Describes a situation in which there is not enough
        power adjustment in the GLSK file to cover the
        capacity.</Definition> </CodeDescription>
    :cvar B37: <CodeDescription xmlns=""> <Title>Voltage
        constraint</Title> <Definition>Describes an N-k or N state
        voltage violation.</Definition> </CodeDescription>
    :cvar B38: <CodeDescription xmlns=""> <Title>Angle
        constraint</Title> <Definition>Describes an N-k or N state angle
        violation.</Definition> </CodeDescription>
    :cvar B39: <CodeDescription xmlns=""> <Title>Stability</Title>
        <Definition>Describes a situation in which the dynamic behaviour
        of the network violated.</Definition> </CodeDescription>
    :cvar B40: <CodeDescription xmlns=""> <Title>Loadflow
        divergence</Title> <Definition>Describes a network situation in
        which the provided capacity values are part of a load flow
        divergence situation.</Definition> </CodeDescription>
    :cvar B41: <CodeDescription xmlns=""> <Title>Exclusion for SoS
        reasons</Title> <Definition>This is the adjustment applied to
        the capacity of a branch to have a minimum RAM (Remaining
        Available Margin) available for commercial
        exchanges.</Definition> </CodeDescription>
    :cvar B42: <CodeDescription xmlns=""> <Title>Constraint by the
        market</Title> <Definition>A constraint due to market
        restrictions.</Definition> </CodeDescription>
    :cvar B43: <CodeDescription xmlns=""> <Title>Ordinary</Title>
        <Definition>The contingency is ordinary (methodology for
        coordinating operational security analysis, article
        6).</Definition> </CodeDescription>
    :cvar B44: <CodeDescription xmlns=""> <Title>Exceptional</Title>
        <Definition>The contingency is exceptional (methodology for
        coordinating operational security analysis, article
        6).</Definition> </CodeDescription>
    :cvar B45: <CodeDescription xmlns=""> <Title>Out of range</Title>
        <Definition>The contingency is out of range (methodology for
        coordinating operational security analysis, article
        6).</Definition> </CodeDescription>
    :cvar B46: <CodeDescription xmlns=""> <Title>Internal
        congestion</Title> <Definition>A temporary congestion within a
        bidding zone or scheduling area.</Definition> </CodeDescription>
    :cvar B47: <CodeDescription xmlns=""> <Title>Operational security
        constraints</Title> <Definition>Operational security constraints
        identified by TSOs.</Definition> </CodeDescription>
    :cvar B48: <CodeDescription xmlns=""> <Title>Estimated value</Title>
        <Definition>Describes a situation where a calculation process
        has failed and extrapolated or interpolated values will be
        applied.</Definition> </CodeDescription>
    :cvar B49: <CodeDescription xmlns=""> <Title>Balancing</Title>
        <Definition>Activated for balancing purposes.</Definition>
        </CodeDescription>
    :cvar B50: <CodeDescription xmlns=""> <Title>Values shared</Title>
        <Definition>Values of this time series are also valid for
        counter-party.</Definition> </CodeDescription>
    :cvar B51: <CodeDescription xmlns=""> <Title>Outside price
        limits</Title> <Definition>The offered price is not within the
        valid limits.</Definition> </CodeDescription>
    :cvar B52: <CodeDescription xmlns=""> <Title>Previous timeframe
        data</Title> <Definition>In case of processing issue, sent data
        are based on the previous timeframe.</Definition>
        </CodeDescription>
    :cvar B53: <CodeDescription xmlns=""> <Title>MOL merging
        succesful</Title> <Definition>The merging of the Merit Order
        List has been successfully processed.</Definition>
        </CodeDescription>
    :cvar B54: <CodeDescription xmlns=""> <Title>MOL merging
        failed</Title> <Definition>The merging of the Merit Order List
        has failed.</Definition> </CodeDescription>
    :cvar B55: <CodeDescription xmlns=""> <Title>Because of
        redispatching</Title> <Definition>Because of redispatching
        according to Article 2(26) of Commission Regulation (EU)
        543/2013</Definition> </CodeDescription>
    :cvar B56: <CodeDescription xmlns=""> <Title>Because of
        countertrading</Title> <Definition>Because of countertrading
        according to Article 2(13) of Commission Regulation (EU)
        543/2013</Definition> </CodeDescription>
    :cvar B57: <CodeDescription xmlns=""> <Title>Because of other
        remedial action</Title> <Definition>Not available because of any
        remedial action.</Definition> </CodeDescription>
    :cvar B58: <CodeDescription xmlns=""> <Title>Insufficiency of
        reserves</Title> <Definition>The reserve capacity is not
        sufficient.</Definition> </CodeDescription>
    :cvar B59: <CodeDescription xmlns=""> <Title>Unavailability of
        reserve providing unit</Title> <Definition>The unit providing
        the reserve is subject to technical unavailability.</Definition>
        </CodeDescription>
    :cvar B60: <CodeDescription xmlns=""> <Title>Unavailability of
        automatic protection systems</Title> <Definition>Unavailability
        of tools to detect predetermined system conditions that have a
        high probability of causing unusual stress on the power system,
        for which pre-planned remedial action is considered necessary or
        for which automatic protective actions may be triggered such as
        special protection schemes or automatic load
        shedding.</Definition> </CodeDescription>
    :cvar B61: <CodeDescription xmlns=""> <Title>Physical cable or
        converter restrictions</Title> <Definition>Limitation due to
        physical cable or converter restrictions.</Definition>
        </CodeDescription>
    :cvar B62: <CodeDescription xmlns=""> <Title>Constraints in
        controller systems</Title> <Definition>Limitation due to
        constraints in controller systems.</Definition>
        </CodeDescription>
    :cvar B63: <CodeDescription xmlns=""> <Title>Adjusted because of
        expected violation of operational security</Title>
        <Definition>The capacity is adjusted because of an expected
        violation of operational security limits of physical
        transmission assets.</Definition> </CodeDescription>
    :cvar B64: <CodeDescription xmlns=""> <Title>Adjusted because
        already considered remedial actions are assessed as not
        sufficient</Title> <Definition>The capacity is adjusted because
        the remedial actions were assessed as not sufficient or
        ineffective to avoid the expected violation of operational
        security limit(s).</Definition> </CodeDescription>
    :cvar B65: <CodeDescription xmlns=""> <Title>Time series partially
        accepted</Title> <Definition>The time series is partially
        accepted.</Definition> </CodeDescription>
    :cvar B66: <CodeDescription xmlns=""> <Title>Demand fully
        netted</Title> <Definition>Demand was fully netted against other
        demand(s).</Definition> </CodeDescription>
    :cvar B67: <CodeDescription xmlns=""> <Title>Bid activated in same
        direction</Title> <Definition>One or several bids were activated
        in the same direction within the same uncongested area as the
        demand.</Definition> </CodeDescription>
    :cvar B68: <CodeDescription xmlns=""> <Title>Optimization in
        progress</Title> <Definition>The activation optimisation
        framework is being executed.</Definition> </CodeDescription>
    :cvar B69: <CodeDescription xmlns=""> <Title>Wrong energy market
        timeframe</Title> <Definition>The given energy market timeframe
        is invalid or wrong.</Definition> </CodeDescription>
    :cvar B70: <CodeDescription xmlns=""> <Title>Message partially
        accepted</Title> <Definition>The detailed transactions of the
        received document are partially accepted. It is necessary to
        look at the detailed (transaction) level to determine if the
        transaction is accepted, rejected etc.</Definition>
        </CodeDescription>
    :cvar B71: <CodeDescription xmlns=""> <Title>(Explicit) Permission
        from the customer</Title> <Definition>Based on the regulation
        (EU) 2016/679 (GDPR) Article 6, Lawfulness of processing: The
        data subject has given consent to the processing of his or her
        personal data for one or more specific purposes.</Definition>
        </CodeDescription>
    :cvar B72: <CodeDescription xmlns=""> <Title>In execution of a
        contract with the customer (Execution of contract)</Title>
        <Definition>Based on the regulation (EU) 2016/679 (GDPR) Article
        6, Lawfulness of processing: Processing is necessary for the
        performance of a contract to which the data subject is party or
        in order to take steps at the request of the data subject prior
        to entering into a contract.</Definition> </CodeDescription>
    :cvar B73: <CodeDescription xmlns=""> <Title>Legal
        obligations</Title> <Definition>Based on the regulation (EU)
        2016/679 (GDPR) Article 6, Lawfulness of processing: Processing
        is necessary for compliance with a legal obligation to which the
        controller is subject.</Definition> </CodeDescription>
    :cvar B74: <CodeDescription xmlns=""> <Title>In protection of vital
        interests of the customer</Title> <Definition>Based on the
        regulation (EU) 2016/679 (GDPR) Article 6, Lawfulness of
        processing: Processing is necessary in order to protect the
        vital interests of the data subject or of another natural
        person. </Definition> </CodeDescription>
    :cvar B75: <CodeDescription xmlns=""> <Title>In order to perform a
        duty of common (national) interest</Title> <Definition>Based on
        the regulation (EU) 2016/679 (GDPR) Article 6, Lawfulness of
        processing: Processing is necessary for the performance of a
        task carried out in the public interest or in the exercise of
        official authority vested in the controller. </Definition>
        </CodeDescription>
    :cvar B76: <CodeDescription xmlns=""> <Title>Justified interest of
        the dataprocessee</Title> <Definition>Based on the regulation
        (EU) 2016/679 (GDPR) Article 6, Lawfulness of processing:
        Processing is necessary for the purposes of the legitimate
        interests pursued by the controller or by a third party, except
        where such interests are overridden by the interests or
        fundamental rights and freedoms of the data subject which
        require protection of personal data, in particular where the
        data subject is a child </Definition> </CodeDescription>
    :cvar B77: <CodeDescription xmlns=""> <Title>Fulfilment of
        purpose</Title> <Definition>The purpose of the object or action
        has been fulfilled.</Definition> </CodeDescription>
    :cvar B78: <CodeDescription xmlns=""> <Title>Reach of end
        timestamp</Title> <Definition>The object or action has reached
        its end timestamp.</Definition> </CodeDescription>
    :cvar B79: <CodeDescription xmlns=""> <Title>Revocation</Title>
        <Definition>Revocation of the action or object.</Definition>
        </CodeDescription>
    :cvar B80: <CodeDescription xmlns=""> <Title>Termination</Title>
        <Definition>Termination of the action or object.</Definition>
        </CodeDescription>
    """

    VALUE_999 = "999"
    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A20 = "A20"
    A21 = "A21"
    A22 = "A22"
    A23 = "A23"
    A24 = "A24"
    A25 = "A25"
    A26 = "A26"
    A27 = "A27"
    A28 = "A28"
    A29 = "A29"
    A30 = "A30"
    A41 = "A41"
    A42 = "A42"
    A43 = "A43"
    A44 = "A44"
    A45 = "A45"
    A46 = "A46"
    A47 = "A47"
    A48 = "A48"
    A49 = "A49"
    A50 = "A50"
    A51 = "A51"
    A52 = "A52"
    A53 = "A53"
    A54 = "A54"
    A55 = "A55"
    A56 = "A56"
    A57 = "A57"
    A58 = "A58"
    A59 = "A59"
    A60 = "A60"
    A61 = "A61"
    A62 = "A62"
    A63 = "A63"
    A64 = "A64"
    A65 = "A65"
    A66 = "A66"
    A67 = "A67"
    A68 = "A68"
    A69 = "A69"
    A70 = "A70"
    A71 = "A71"
    A72 = "A72"
    A73 = "A73"
    A74 = "A74"
    A75 = "A75"
    A76 = "A76"
    A77 = "A77"
    A78 = "A78"
    A79 = "A79"
    A80 = "A80"
    A81 = "A81"
    A82 = "A82"
    A83 = "A83"
    A84 = "A84"
    A85 = "A85"
    A86 = "A86"
    A87 = "A87"
    A88 = "A88"
    A89 = "A89"
    A90 = "A90"
    A91 = "A91"
    A92 = "A92"
    A93 = "A93"
    A94 = "A94"
    A95 = "A95"
    A96 = "A96"
    A97 = "A97"
    A98 = "A98"
    A99 = "A99"
    B01 = "B01"
    B02 = "B02"
    B03 = "B03"
    B04 = "B04"
    B05 = "B05"
    B06 = "B06"
    B07 = "B07"
    B08 = "B08"
    B09 = "B09"
    B10 = "B10"
    B11 = "B11"
    B12 = "B12"
    B13 = "B13"
    B14 = "B14"
    B15 = "B15"
    B16 = "B16"
    B17 = "B17"
    B18 = "B18"
    B19 = "B19"
    B20 = "B20"
    B21 = "B21"
    B22 = "B22"
    B23 = "B23"
    B24 = "B24"
    B25 = "B25"
    B26 = "B26"
    B27 = "B27"
    B28 = "B28"
    B29 = "B29"
    B30 = "B30"
    B31 = "B31"
    B32 = "B32"
    B33 = "B33"
    B34 = "B34"
    B35 = "B35"
    B36 = "B36"
    B37 = "B37"
    B38 = "B38"
    B39 = "B39"
    B40 = "B40"
    B41 = "B41"
    B42 = "B42"
    B43 = "B43"
    B44 = "B44"
    B45 = "B45"
    B46 = "B46"
    B47 = "B47"
    B48 = "B48"
    B49 = "B49"
    B50 = "B50"
    B51 = "B51"
    B52 = "B52"
    B53 = "B53"
    B54 = "B54"
    B55 = "B55"
    B56 = "B56"
    B57 = "B57"
    B58 = "B58"
    B59 = "B59"
    B60 = "B60"
    B61 = "B61"
    B62 = "B62"
    B63 = "B63"
    B64 = "B64"
    B65 = "B65"
    B66 = "B66"
    B67 = "B67"
    B68 = "B68"
    B69 = "B69"
    B70 = "B70"
    B71 = "B71"
    B72 = "B72"
    B73 = "B73"
    B74 = "B74"
    B75 = "B75"
    B76 = "B76"
    B77 = "B77"
    B78 = "B78"
    B79 = "B79"
    B80 = "B80"


class RightsTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Use It Or Lose
        It</Title> <Definition>Any rights not nominated shall be
        lost.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Use It Or Sell
        It</Title> <Definition>Any rights that are not nominated shall
        be sold.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Allocation curtailment
        possible</Title> <Definition>Rights acquired may be
        curtailed.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Nomination curtailment
        possible</Title> <Definition>Rights acquired may be curtailed at
        nomination.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Resale possible</Title>
        <Definition>Acquired rights may be resold.</Definition>
        </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Transfer
        possible</Title> <Definition>Acquired rights may be
        transferred.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"


class RoleTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Trade responsible
        party</Title> <Definition>Refer to role model definitions in the
        ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Consumption responsible
        party</Title> <Definition>Refer to role model definitions in the
        ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Combined power exchange
        (not to be used)</Title> <Definition>This role is no longer in
        the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>System operator</Title>
        <Definition>Refer to role model definitions in the ENTSO-E
        Harmonised Role Model Document.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Imbalance settlement
        responsible</Title> <Definition>Refer to role model definitions
        in the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Production responsible
        party</Title> <Definition>Refer to role model definitions in the
        ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Transmission capacity
        allocator</Title> <Definition>Refer to role model definitions in
        the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Balance responsible
        party</Title> <Definition>Refer to role model definitions in the
        ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>Metered data
        aggregator</Title> <Definition>Refer to role model definitions
        in the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Billing agent</Title>
        <Definition>Refer to role model definitions in the ENTSO-E
        Harmonised Role Model Document.</Definition> </CodeDescription>
    :cvar A11: <CodeDescription xmlns=""> <Title>Market operator</Title>
        <Definition>Refer to role model definitions in the ENTSO-E
        Harmonised Role Model Document.</Definition> </CodeDescription>
    :cvar A12: <CodeDescription xmlns=""> <Title>Energy supplier</Title>
        <Definition>Refer to role model definitions in the ENTSO-E
        Harmonised Role Model Document.</Definition> </CodeDescription>
    :cvar A13: <CodeDescription xmlns=""> <Title>Consumer</Title>
        <Definition>Refer to role model definitions in the ENTSO-E
        Harmonised Role Model Document.</Definition> </CodeDescription>
    :cvar A14: <CodeDescription xmlns=""> <Title>Control area
        operator</Title> <Definition>Refer to role model definitions in
        the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A15: <CodeDescription xmlns=""> <Title>Control block
        operator</Title> <Definition>Refer to role model definitions in
        the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A16: <CodeDescription xmlns=""> <Title>Coordination centre
        operator</Title> <Definition>Refer to role model definitions in
        the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A17: <CodeDescription xmlns=""> <Title>Grid access
        provider</Title> <Definition>Refer to role model definitions in
        the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A18: <CodeDescription xmlns=""> <Title>Grid operator</Title>
        <Definition>Refer to role model definitions in the ENTSO-E
        Harmonised Role Model Document.</Definition> </CodeDescription>
    :cvar A19: <CodeDescription xmlns=""> <Title>Meter
        administrator</Title> <Definition>Refer to role model
        definitions in the ENTSO-E Harmonised Role Model
        Document.</Definition> </CodeDescription>
    :cvar A20: <CodeDescription xmlns=""> <Title>Party connected to
        grid</Title> <Definition>Refer to role model definitions in the
        ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A21: <CodeDescription xmlns=""> <Title>Producer</Title>
        <Definition>Refer to role model definitions in the ENTSO-E
        Harmonised Role Model Document.</Definition> </CodeDescription>
    :cvar A22: <CodeDescription xmlns=""> <Title>Profile maintenance
        party</Title> <Definition>Refer to role model definitions in the
        ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A23: <CodeDescription xmlns=""> <Title>Meter operator</Title>
        <Definition>Refer to role model definitions in the ENTSO-E
        Harmonised Role Model Document.</Definition> </CodeDescription>
    :cvar A24: <CodeDescription xmlns=""> <Title>Metered data
        collector</Title> <Definition>Refer to role model definitions in
        the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A25: <CodeDescription xmlns=""> <Title>Metered data
        responsible</Title> <Definition>Refer to role model definitions
        in the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A26: <CodeDescription xmlns=""> <Title>Metering point
        administrator</Title> <Definition>Refer to role model
        definitions in the ENTSO-E Harmonised Role Model
        Document.</Definition> </CodeDescription>
    :cvar A27: <CodeDescription xmlns=""> <Title>Resource
        Provider</Title> <Definition>Refer to role model definitions in
        the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A28: <CodeDescription xmlns=""> <Title>Scheduling
        coordinator</Title> <Definition>Refer to role model definitions
        in the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A29: <CodeDescription xmlns=""> <Title>Capacity Trader</Title>
        <Definition>Refer to role model definitions in the ENTSO-E
        Harmonised Role Model Document.</Definition> </CodeDescription>
    :cvar A30: <CodeDescription xmlns=""> <Title>Interconnection Trade
        Responsible</Title> <Definition>Refer to role model definitions
        in the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A31: <CodeDescription xmlns=""> <Title>Nomination
        Validator</Title> <Definition>Refer to role model definitions in
        the ENTSO-E Harmonised Role Model Document.</Definition>
        </CodeDescription>
    :cvar A32: <CodeDescription xmlns=""> <Title>Market information
        aggregator</Title> <Definition>Refer to role model definitions
        in the ENTSO-E Harmonised Role Model Document. A party that
        collects information from different sources and assembles  it to
        provide a summary of the market.</Definition> </CodeDescription>
    :cvar A33: <CodeDescription xmlns=""> <Title>Information
        receiver</Title> <Definition>Refer to role model definitions in
        the ENTSO-E Harmonised Role Model Document. A party, not
        necessarily a market participant, which receives information
        about the market.</Definition> </CodeDescription>
    :cvar A34: <CodeDescription xmlns=""> <Title>Reserve
        Allocator</Title> <Definition>Refer to role model definitions in
        the ENTSO-E Harmonised Role Model Document. A party that informs
        the market of reserve requirements, receives tenders against the
        requirements and in compliance with the prequalification
        criteria, determines what tenders meet requirements and assigns
        tenders.</Definition> </CodeDescription>
    :cvar A35: <CodeDescription xmlns=""> <Title>MOL Responsible</Title>
        <Definition>Refer to role model definitions in the ENTSO-E
        Harmonised Role Model Document. A party that Informs the market
        of reserve requirements, receives tenders against the
        requirements and in compliance with the prequalification
        criteria, determines what tenders meet requirements and assigns
        tenders.</Definition> </CodeDescription>
    :cvar A36: <CodeDescription xmlns=""> <Title>Capacity
        Coordinator</Title> <Definition>A party, acting on behalf of the
        SOs involved, responsible for establishing a coordinated Offered
        Capacity and/or NTC and/or ATC between several Scheduling
        Areas.</Definition> </CodeDescription>
    :cvar A37: <CodeDescription xmlns=""> <Title>Reconciliation
        Accountable</Title> <Definition>Refer to role model definitions
        in the ENTSO-E Harmonised Role Model Document. A party that is
        financially accountable for the reconciled volume of energy
        products for a profiled local metering point.</Definition>
        </CodeDescription>
    :cvar A38: <CodeDescription xmlns=""> <Title>Reconciliation
        Responsible</Title> <Definition>A party that is responsible for
        reconciling, within a metering grid area, the volumes used in
        the imbalance settlement process for profiled metering points
        and the actual metered quantities.</Definition>
        </CodeDescription>
    :cvar A39: <CodeDescription xmlns=""> <Title>Data provider</Title>
        <Definition>A party that is responsible for providing
        information to a central authority.</Definition>
        </CodeDescription>
    :cvar A40: <CodeDescription xmlns=""> <Title>Local Issuing Office
        (LIO)</Title> <Definition>A party that is responsible for
        operating a Local Issuing Office (LIO).</Definition>
        </CodeDescription>
    :cvar A41: <CodeDescription xmlns=""> <Title>Central Issuing Office
        (CIO)</Title> <Definition>A party that is responsible for
        operating a Central Issuing Office (CIO).</Definition>
        </CodeDescription>
    :cvar A42: <CodeDescription xmlns=""> <Title>EIC Participant</Title>
        <Definition>A party that participates in the EIC
        environment.</Definition> </CodeDescription>
    :cvar A43: <CodeDescription xmlns=""> <Title>Weather
        analyser</Title> <Definition>A party that analyses the current
        and forecast weather situation and establishes a prognosis of
        its impact on the renewable energy environment as well as the
        overall load.</Definition> </CodeDescription>
    :cvar A44: <CodeDescription xmlns=""> <Title>Regional Security
        Coordinator (RSC)</Title> <Definition>The RSC as defined in the
        System Operation guideline.</Definition> </CodeDescription>
    :cvar A45: <CodeDescription xmlns=""> <Title>Energy Service Company
        (ESCO)</Title> <Definition>A party offering energy-related
        services to the Party Connected to Grid, but not directly active
        in the energy value chain or the physical infrastructure itself.
        The ESCO may provide insight services as well as energy
        management services.</Definition> </CodeDescription>
    :cvar A46: <CodeDescription xmlns=""> <Title>Balancing Service
        Provider</Title> <Definition>A party with reserve-providing
        units or reserve-providing groups able to provide balancing
        services to LFC Operators.</Definition> </CodeDescription>
    :cvar A47: <CodeDescription xmlns=""> <Title>Energy trader</Title>
        <Definition>A party that is selling or buying
        energy.</Definition> </CodeDescription>
    :cvar A48: <CodeDescription xmlns=""> <Title>LFC Operator</Title>
        <Definition>A party that is responsible for the Load Frequency
        Control of its LFC Area or LFC Block.</Definition>
        </CodeDescription>
    :cvar A49: <CodeDescription xmlns=""> <Title>Transmission System
        Operator (TSO)</Title> <Definition>The Transmission System
        Operator (TSO) is responsible for the transport of electricity
        on the extra high-voltage and high-voltage interconnected
        system. This is a market participant and not a role in
        Harmonised Role Model.</Definition> </CodeDescription>
    :cvar A50: <CodeDescription xmlns=""> <Title>Distribution System
        Operator (DSO)</Title> <Definition>Distribution System Operator
        (DSO) is responsible for transport of electricity on high-
        voltage (optionally), medium-voltage and low-voltage
        distribution systems. This is a market participant and not a
        role in Harmonised Role Model.</Definition> </CodeDescription>
    :cvar A51: <CodeDescription xmlns=""> <Title>Resource Capacity
        Mechanism Operator</Title> <Definition>Resource capacity
        mechanism operator is the party responsible to operate the
        resource capacity mechanism in a member state. It can either be
        the TSO or an independent party.</Definition> </CodeDescription>
    :cvar A52: <CodeDescription xmlns=""> <Title>Resource
        aggregator</Title> <Definition>A party that aggregates resources
        for usage by a service provider for energy market
        services.</Definition> </CodeDescription>
    :cvar A53: <CodeDescription xmlns=""> <Title>Cost sharing
        calculator</Title> <Definition>A party responsible for the
        mapping of the costs between areas and parties.</Definition>
        </CodeDescription>
    :cvar A54: <CodeDescription xmlns=""> <Title>Settlement
        responsible</Title> <Definition>A party responsible for settling
        the costs.</Definition> </CodeDescription>
    :cvar A55: <CodeDescription xmlns=""> <Title>Coordinated Capacity
        Calculator</Title> <Definition>Coordinated Capacity Calculator
        is the entity or entities with the task of calculating
        transmission capacity, at regional level or above.</Definition>
        </CodeDescription>
    :cvar A56: <CodeDescription xmlns=""> <Title>Flexibility service
        provider</Title> <Definition>A party that offers flexibility
        services based on acquired (aggregated) resources. </Definition>
        </CodeDescription>
    :cvar A57: <CodeDescription xmlns=""> <Title>Data access
        provider</Title> <Definition>A party responsible for
        facilitating access to data.</Definition> </CodeDescription>
    :cvar A58: <CodeDescription xmlns=""> <Title>Metered data
        administrator</Title> <Definition>A party responsible for
        storing and distributing validated measured data.</Definition>
        </CodeDescription>
    :cvar A59: <CodeDescription xmlns=""> <Title>Permission
        administrator</Title> <Definition>A party responsible for
        administrating a register of data access permissions for a set
        of metering points, making this information available to final
        customers and eligible parties in the sector, on
        request.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"
    A13 = "A13"
    A14 = "A14"
    A15 = "A15"
    A16 = "A16"
    A17 = "A17"
    A18 = "A18"
    A19 = "A19"
    A20 = "A20"
    A21 = "A21"
    A22 = "A22"
    A23 = "A23"
    A24 = "A24"
    A25 = "A25"
    A26 = "A26"
    A27 = "A27"
    A28 = "A28"
    A29 = "A29"
    A30 = "A30"
    A31 = "A31"
    A32 = "A32"
    A33 = "A33"
    A34 = "A34"
    A35 = "A35"
    A36 = "A36"
    A37 = "A37"
    A38 = "A38"
    A39 = "A39"
    A40 = "A40"
    A41 = "A41"
    A42 = "A42"
    A43 = "A43"
    A44 = "A44"
    A45 = "A45"
    A46 = "A46"
    A47 = "A47"
    A48 = "A48"
    A49 = "A49"
    A50 = "A50"
    A51 = "A51"
    A52 = "A52"
    A53 = "A53"
    A54 = "A54"
    A55 = "A55"
    A56 = "A56"
    A57 = "A57"
    A58 = "A58"
    A59 = "A59"


class StatusTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Intermediate</Title>
        <Definition>The document is in a non finalized
        state.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Final</Title>
        <Definition>The document is in a definitive state.</Definition>
        </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Deactivated</Title>
        <Definition>The object being reported has been
        deactivated.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Reactivated</Title>
        <Definition>The object being reported has been
        reactivated.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Active</Title>
        <Definition>The object being reported is currently
        active.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Available</Title>
        <Definition>The volumes (one or more) are
        available.</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Activated</Title>
        <Definition>The quantities in the time series have been
        activated.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>In process</Title>
        <Definition>The quantities in the time series are in the process
        of activation (an activation request has been
        made).</Definition> </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>Cancelled</Title>
        <Definition>The tender indicated in the time series has been
        completely cancelled. In this case the resources are no longer
        available to all Acquiring System Operators</Definition>
        </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Ordered</Title>
        <Definition>The quantities in the time series are to be
        activated.</Definition> </CodeDescription>
    :cvar A11: <CodeDescription xmlns=""> <Title>Unavailable</Title>
        <Definition>The volumes (one or more) are
        unavailable.</Definition> </CodeDescription>
    :cvar A12: <CodeDescription xmlns=""> <Title>RGCE agreed</Title>
        <Definition>The information has been agreed within the ENTSO-E
        Regional Group Continental Europe process.</Definition>
        </CodeDescription>
    :cvar A13: <CodeDescription xmlns=""> <Title>Withdrawn</Title>
        <Definition>The information or action has been withdrawn by the
        submitter.</Definition> </CodeDescription>
    :cvar A14: <CodeDescription xmlns=""> <Title>Creation</Title>
        <Definition>The action requested to be carried out is the
        creation of a new object.</Definition> </CodeDescription>
    :cvar A15: <CodeDescription xmlns=""> <Title>Update</Title>
        <Definition>The action requested to be carried out is the update
        an existing object.</Definition> </CodeDescription>
    :cvar A16: <CodeDescription xmlns=""> <Title>Deactivation</Title>
        <Definition>The action requested to be carried out is to
        deactivate an existing object.</Definition> </CodeDescription>
    :cvar A17: <CodeDescription xmlns=""> <Title>Reactivation</Title>
        <Definition>The action requested to be carried out is to
        reactivate a previously deactivated object.</Definition>
        </CodeDescription>
    :cvar A18: <CodeDescription xmlns=""> <Title>Preventive</Title>
        <Definition>The remedial action is applied to prevent an
        outage.</Definition> </CodeDescription>
    :cvar A19: <CodeDescription xmlns=""> <Title>Curative</Title>
        <Definition>The remedial action is applied after an outage has
        occurred, in order to maintain the operational
        security.</Definition> </CodeDescription>
    :cvar A20: <CodeDescription xmlns=""> <Title>Automatic</Title>
        <Definition>The remedial action being described is applied by an
        automation when an outage occurs.</Definition>
        </CodeDescription>
    :cvar A21: <CodeDescription xmlns=""> <Title>Open</Title>
        <Definition>The action being described consists of disconnecting
        the network element  to the transmission network.</Definition>
        </CodeDescription>
    :cvar A22: <CodeDescription xmlns=""> <Title>Close</Title>
        <Definition>The action being described consists of connecting
        the network element  to the transmission network.</Definition>
        </CodeDescription>
    :cvar A23: <CodeDescription xmlns=""> <Title>Stop</Title>
        <Definition>The action being described consists of stopping the
        production or consumption connected to a network
        element.</Definition> </CodeDescription>
    :cvar A24: <CodeDescription xmlns=""> <Title>Start</Title>
        <Definition>The action being described consists of starting the
        production or consumption connected to a network
        element.</Definition> </CodeDescription>
    :cvar A25: <CodeDescription xmlns=""> <Title>Relative</Title>
        <Definition>The quantity being described is a relative value to
        an initial state.</Definition> </CodeDescription>
    :cvar A26: <CodeDescription xmlns=""> <Title>Absolute</Title>
        <Definition>The quantity being described is an absolute
        value.</Definition> </CodeDescription>
    :cvar A27: <CodeDescription xmlns=""> <Title>Curative or
        preventive</Title> <Definition>The remedial action can be
        applied to prevent an outage or after an outage has occurred in
        order to maintain the operational security.</Definition>
        </CodeDescription>
    :cvar A28: <CodeDescription xmlns=""> <Title>Unshared bid</Title>
        <Definition>Used to indicate that the bid cannot be
        shared.</Definition> </CodeDescription>
    :cvar A29: <CodeDescription xmlns=""> <Title>Pre Processed</Title>
        <Definition>to be process</Definition> </CodeDescription>
    :cvar A30: <CodeDescription xmlns=""> <Title>Substituted</Title>
        <Definition>Substituted pre-processing data.</Definition>
        </CodeDescription>
    :cvar A31: <CodeDescription xmlns=""> <Title>Modified</Title>
        <Definition>Modified pre-processing data by RSC or CGMA
        platform.</Definition> </CodeDescription>
    :cvar A32: <CodeDescription xmlns=""> <Title>Result</Title>
        <Definition>Result</Definition> </CodeDescription>
    :cvar A33: <CodeDescription xmlns=""> <Title>Not satisfied</Title>
        <Definition>The need described in the time series cannot be
        satisfied.</Definition> </CodeDescription>
    :cvar A34: <CodeDescription xmlns=""> <Title>Rejected</Title>
        <Definition>The document rejected by one or more
        parties.</Definition> </CodeDescription>
    :cvar A35: <CodeDescription xmlns=""> <Title>Preliminary</Title>
        <Definition>Indicative information only for initial planning
        purposes.</Definition> </CodeDescription>
    :cvar A36: <CodeDescription xmlns=""> <Title>Planned</Title>
        <Definition>Is planned.</Definition> </CodeDescription>
    :cvar A37: <CodeDescription xmlns=""> <Title>Confirmed</Title>
        <Definition>The status is  confirmed.</Definition>
        </CodeDescription>
    :cvar A38: <CodeDescription xmlns=""> <Title>Shall Be Used</Title>
        <Definition>The object defined in the series shall be
        used.</Definition> </CodeDescription>
    :cvar A39: <CodeDescription xmlns=""> <Title>Could Be Used</Title>
        <Definition>The object defined in the series could be
        used.</Definition> </CodeDescription>
    :cvar A40: <CodeDescription xmlns=""> <Title>Proposed</Title>
        <Definition>The status of the information is
        proposed.</Definition> </CodeDescription>
    :cvar A41: <CodeDescription xmlns=""> <Title>Individual Network
        Data</Title> <Definition>The network data provided in the
        document or series concerns the the unique TSO area describes by
        the document or series.</Definition> </CodeDescription>
    :cvar A42: <CodeDescription xmlns=""> <Title>Common Network
        Data</Title> <Definition>The network data provided in the
        document or series concerns the whole area describes by the
        document or series.</Definition> </CodeDescription>
    :cvar A43: <CodeDescription xmlns=""> <Title>Setpoint
        schedule</Title> <Definition>The code for the power setpoint
        mode of operation of the HVDC link.</Definition>
        </CodeDescription>
    :cvar A44: <CodeDescription xmlns=""> <Title>Proportional external
        signal</Title> <Definition>The code for the proportional
        external signal mode of operation of the HVDC link.</Definition>
        </CodeDescription>
    :cvar A45: <CodeDescription xmlns=""> <Title>AC emulation</Title>
        <Definition>The code for the AC emulation mode of operation of
        the HVDC link.</Definition> </CodeDescription>
    :cvar A46: <CodeDescription xmlns=""> <Title>Importing
        element</Title> <Definition>An importing network element in
        which the flow measurement enters.</Definition>
        </CodeDescription>
    :cvar A47: <CodeDescription xmlns=""> <Title>Exporting
        element</Title> <Definition>An exporting network element from
        which the flow measurement comes out.</Definition>
        </CodeDescription>
    :cvar A48: <CodeDescription xmlns=""> <Title>To be optimized</Title>
        <Definition>Describes an element which needs to be optimized by
        an optimization process.</Definition> </CodeDescription>
    :cvar A49: <CodeDescription xmlns=""> <Title>To be monitored</Title>
        <Definition>Describes an element which needs to be monitored by
        an optimization process.</Definition> </CodeDescription>
    :cvar A50: <CodeDescription xmlns=""> <Title>To be included in
        capacity calculation</Title> <Definition>Describes an element
        which needs to be taken into account in a capacity calculation
        process.</Definition> </CodeDescription>
    :cvar A51: <CodeDescription xmlns=""> <Title>Relative to previous
        point in time</Title> <Definition>The quantity being described
        is a relative value to a previous point in time.</Definition>
        </CodeDescription>
    :cvar A52: <CodeDescription xmlns=""> <Title>For flow
        optimization</Title> <Definition>Describes an element which
        needs to be optimized by a flow optimization
        process.</Definition> </CodeDescription>
    :cvar A53: <CodeDescription xmlns=""> <Title>For voltage
        optimization</Title> <Definition>Describes an element which
        needs to be optimized by a voltage optimization
        process.</Definition> </CodeDescription>
    :cvar A54: <CodeDescription xmlns=""> <Title>Presolved</Title>
        <Definition>Describes an active constraint that limits the
        exchanges. It is part of the presolved domain.</Definition>
        </CodeDescription>
    :cvar A55: <CodeDescription xmlns=""> <Title>Not available if linked
        bid activated</Title> <Definition>Bid not available if linked
        bid activated.</Definition> </CodeDescription>
    :cvar A56: <CodeDescription xmlns=""> <Title>Not available if linked
        bid rejected</Title> <Definition>Bid not available if linked bid
        rejected.</Definition> </CodeDescription>
    :cvar A57: <CodeDescription xmlns=""> <Title>Not available for DA if
        linked bid subject to DA</Title> <Definition>Bid not available
        for direct activation if linked bid subject to direct
        activation.</Definition> </CodeDescription>
    :cvar A58: <CodeDescription xmlns=""> <Title>Not available for DA if
        linked bid subject to SA</Title> <Definition>Bid not available
        for direct activation if linked bid subject to scheduled
        activation.</Definition> </CodeDescription>
    :cvar A59: <CodeDescription xmlns=""> <Title>Not available if linked
        bid subject to SA</Title> <Definition>Bid not available if
        linked bid subject to scheduled activation.</Definition>
        </CodeDescription>
    :cvar A60: <CodeDescription xmlns=""> <Title>Not available if linked
        bid subject to DA</Title> <Definition>Bid not available if
        linked bid subject to direct activation.</Definition>
        </CodeDescription>
    :cvar A61: <CodeDescription xmlns=""> <Title>Primary market</Title>
        <Definition>A value is traded for the first time.</Definition>
        </CodeDescription>
    :cvar A62: <CodeDescription xmlns=""> <Title>Secondary
        market</Title> <Definition>A value is traded for the second or
        next times between two parties.</Definition> </CodeDescription>
    :cvar A63: <CodeDescription xmlns=""> <Title>Interesting</Title>
        <Definition>Describes an asset which is considered as
        interesting.</Definition> </CodeDescription>
    :cvar A64: <CodeDescription xmlns=""> <Title>Relevant</Title>
        <Definition>Describes an asset which is considered as
        relevant.</Definition> </CodeDescription>
    :cvar A65: <CodeDescription xmlns=""> <Title>Conditionally
        available</Title> <Definition>Bid available as long as none of
        the conditions associated with the linked bids
        materialise.</Definition> </CodeDescription>
    :cvar A66: <CodeDescription xmlns=""> <Title>Conditionally
        unavailable</Title> <Definition>Bid unavailable as long as none
        of the conditions associated with the linked bids
        materialise.</Definition> </CodeDescription>
    :cvar A67: <CodeDescription xmlns=""> <Title>Available if linked bid
        activated</Title> <Definition>Bid available if linked bid
        activated.</Definition> </CodeDescription>
    :cvar A68: <CodeDescription xmlns=""> <Title>Available if linked bid
        rejected</Title> <Definition>Bid available if linked bid
        rejected.</Definition> </CodeDescription>
    :cvar A69: <CodeDescription xmlns=""> <Title>Available if linked bid
        subject to SA</Title> <Definition>Bid available if linked bid
        subject to scheduled activation.</Definition> </CodeDescription>
    :cvar A70: <CodeDescription xmlns=""> <Title>Available if linked bid
        subject to DA</Title> <Definition>Bid available if linked bid
        subject to direct activation.</Definition> </CodeDescription>
    :cvar A71: <CodeDescription xmlns=""> <Title>Available for DA if
        linked bid subject to DA</Title> <Definition>Bid available for
        direct activation if linked bid subject to direct
        activation.</Definition> </CodeDescription>
    :cvar A72: <CodeDescription xmlns=""> <Title>Available for DA if
        linked bid subject to SA</Title> <Definition>Bid available for
        direct activation if linked bid subject to scheduled
        activation.</Definition> </CodeDescription>
    :cvar A73: <CodeDescription xmlns=""> <Title>Delta</Title>
        <Definition>Describes a status representing a difference between
        two values.</Definition> </CodeDescription>
    :cvar A74: <CodeDescription xmlns=""> <Title>Validated</Title>
        <Definition>The object or action was validated.</Definition>
        </CodeDescription>
    :cvar A75: <CodeDescription xmlns=""> <Title>Invalid</Title>
        <Definition>The object or action was invalid.</Definition>
        </CodeDescription>
    :cvar A76: <CodeDescription xmlns=""> <Title>Timed out</Title>
        <Definition>The object or action was timed out.</Definition>
        </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"
    A13 = "A13"
    A14 = "A14"
    A15 = "A15"
    A16 = "A16"
    A17 = "A17"
    A18 = "A18"
    A19 = "A19"
    A20 = "A20"
    A21 = "A21"
    A22 = "A22"
    A23 = "A23"
    A24 = "A24"
    A25 = "A25"
    A26 = "A26"
    A27 = "A27"
    A28 = "A28"
    A29 = "A29"
    A30 = "A30"
    A31 = "A31"
    A32 = "A32"
    A33 = "A33"
    A34 = "A34"
    A35 = "A35"
    A36 = "A36"
    A37 = "A37"
    A38 = "A38"
    A39 = "A39"
    A40 = "A40"
    A41 = "A41"
    A42 = "A42"
    A43 = "A43"
    A44 = "A44"
    A45 = "A45"
    A46 = "A46"
    A47 = "A47"
    A48 = "A48"
    A49 = "A49"
    A50 = "A50"
    A51 = "A51"
    A52 = "A52"
    A53 = "A53"
    A54 = "A54"
    A55 = "A55"
    A56 = "A56"
    A57 = "A57"
    A58 = "A58"
    A59 = "A59"
    A60 = "A60"
    A61 = "A61"
    A62 = "A62"
    A63 = "A63"
    A64 = "A64"
    A65 = "A65"
    A66 = "A66"
    A67 = "A67"
    A68 = "A68"
    A69 = "A69"
    A70 = "A70"
    A71 = "A71"
    A72 = "A72"
    A73 = "A73"
    A74 = "A74"
    A75 = "A75"
    A76 = "A76"


class TarifTypeTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Winter HT</Title>
        <Definition>Winter HT tariff.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Winter HHT</Title>
        <Definition>Winter HHT tariff.</Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Winter NT</Title>
        <Definition>Winter NT tariff.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Summer HT</Title>
        <Definition>Summer HT tariff.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Summer HHT1</Title>
        <Definition>Summer HHT1 tariff.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Summer HHT2</Title>
        <Definition>Summer HHT2 tariff.</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Summer NT</Title>
        <Definition>Summer NT tariff.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"


class TimeframeTypeList(Enum):
    """
    :cvar A01: <CodeDescription xmlns=""> <Title>Real time</Title>
        <Definition>The information provided concerns real time
        timeframe.</Definition> </CodeDescription>
    :cvar A02: <CodeDescription xmlns=""> <Title>Intraday</Title>
        <Definition>The information provided concerns an intra day
        timeframe. </Definition> </CodeDescription>
    :cvar A03: <CodeDescription xmlns=""> <Title>Hour-1</Title>
        <Definition>The information provided concerns 1 hour ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A04: <CodeDescription xmlns=""> <Title>Hour-2</Title>
        <Definition>The information provided concerns 2 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A05: <CodeDescription xmlns=""> <Title>Hour-3</Title>
        <Definition>The information provided concerns 3 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A06: <CodeDescription xmlns=""> <Title>Hour-4</Title>
        <Definition>The information provided concerns 4 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A07: <CodeDescription xmlns=""> <Title>Hour-5</Title>
        <Definition>The information provided concerns 5 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A08: <CodeDescription xmlns=""> <Title>Hour-6</Title>
        <Definition>The information provided concerns 6 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A09: <CodeDescription xmlns=""> <Title>Hour-7</Title>
        <Definition>The information provided concerns 7 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A10: <CodeDescription xmlns=""> <Title>Hour-8</Title>
        <Definition>The information provided concerns 8 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A11: <CodeDescription xmlns=""> <Title>Hour-9</Title>
        <Definition>The information provided concerns 9 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A12: <CodeDescription xmlns=""> <Title>Hour-10</Title>
        <Definition>The information provided concerns 10 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A13: <CodeDescription xmlns=""> <Title>Hour-11</Title>
        <Definition>The information provided concerns 11 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A14: <CodeDescription xmlns=""> <Title>Hour-12</Title>
        <Definition>The information provided concerns 12 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A15: <CodeDescription xmlns=""> <Title>Hour-13</Title>
        <Definition>The information provided concerns 13 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A16: <CodeDescription xmlns=""> <Title>Hour-14</Title>
        <Definition>The information provided concerns 14 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A17: <CodeDescription xmlns=""> <Title>Hour-15</Title>
        <Definition>The information provided concerns 15 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A18: <CodeDescription xmlns=""> <Title>Hour-16</Title>
        <Definition>The information provided concerns 16 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A19: <CodeDescription xmlns=""> <Title>Hour-17</Title>
        <Definition>The information provided concerns 17 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A20: <CodeDescription xmlns=""> <Title>Hour-18</Title>
        <Definition>The information provided concerns 18 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A21: <CodeDescription xmlns=""> <Title>Hour-19</Title>
        <Definition>The information provided concerns 19 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A22: <CodeDescription xmlns=""> <Title>Hour-20</Title>
        <Definition>The information provided concerns 20 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A23: <CodeDescription xmlns=""> <Title>Hour-21</Title>
        <Definition>The information provided concerns 21 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A24: <CodeDescription xmlns=""> <Title>Hour-22</Title>
        <Definition>The information provided concerns 22 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A25: <CodeDescription xmlns=""> <Title>Hour-23</Title>
        <Definition>The information provided concerns 23 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A26: <CodeDescription xmlns=""> <Title>Hour-24</Title>
        <Definition>The information provided concerns 24 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A27: <CodeDescription xmlns=""> <Title>Hour-25</Title>
        <Definition>The information provided concerns 25 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A28: <CodeDescription xmlns=""> <Title>Hour-26</Title>
        <Definition>The information provided concerns 26 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A29: <CodeDescription xmlns=""> <Title>Hour-27</Title>
        <Definition>The information provided concerns 27 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A30: <CodeDescription xmlns=""> <Title>Hour-28</Title>
        <Definition>The information provided concerns 28 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A31: <CodeDescription xmlns=""> <Title>Hour-29</Title>
        <Definition>The information provided concerns 29 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A32: <CodeDescription xmlns=""> <Title>Hour-30</Title>
        <Definition>The information provided concerns 30 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A33: <CodeDescription xmlns=""> <Title>Hour-31</Title>
        <Definition>The information provided concerns 31 hours ahead for
        given delivery hour.</Definition> </CodeDescription>
    :cvar A34: <CodeDescription xmlns=""> <Title>Day ahead</Title>
        <Definition>The information provided concerns day ahead
        timeframe.</Definition> </CodeDescription>
    :cvar A35: <CodeDescription xmlns=""> <Title>Day-2</Title>
        <Definition>The information provided concerns two days ahead
        timeframe. </Definition> </CodeDescription>
    :cvar A36: <CodeDescription xmlns=""> <Title>Day-3</Title>
        <Definition>The information provided concerns three days ahead
        timeframe. </Definition> </CodeDescription>
    :cvar A37: <CodeDescription xmlns=""> <Title>Day-4</Title>
        <Definition>The information provided concerns four days ahead
        timeframe.</Definition> </CodeDescription>
    :cvar A38: <CodeDescription xmlns=""> <Title>Day-5</Title>
        <Definition>The information provided concerns five days ahead
        timeframe. </Definition> </CodeDescription>
    :cvar A39: <CodeDescription xmlns=""> <Title>Day-6</Title>
        <Definition>The information provided concerns six days ahead
        timeframe. </Definition> </CodeDescription>
    :cvar A40: <CodeDescription xmlns=""> <Title>Day-7</Title>
        <Definition>The information provided concerns seven days ahead
        timeframe. </Definition> </CodeDescription>
    :cvar A41: <CodeDescription xmlns=""> <Title>Week ahead</Title>
        <Definition>The information provided concerns next week ahead
        timeframe.</Definition> </CodeDescription>
    :cvar A42: <CodeDescription xmlns=""> <Title>Week-0</Title>
        <Definition>The information provided concerns current week
        timeframe. </Definition> </CodeDescription>
    :cvar A43: <CodeDescription xmlns=""> <Title>Week+1</Title>
        <Definition>The information provided concerns previous week
        timeframe. </Definition> </CodeDescription>
    :cvar A44: <CodeDescription xmlns=""> <Title>Month ahead</Title>
        <Definition>The information provided concerns month ahead
        timeframe. </Definition> </CodeDescription>
    :cvar A45: <CodeDescription xmlns=""> <Title>Year ahead</Title>
        <Definition>The information provided concerns year ahead
        timeframe.</Definition> </CodeDescription>
    :cvar A46: <CodeDescription xmlns=""> <Title>Year-10</Title>
        <Definition>The information provided concerns 10 years ahead
        timeframe.</Definition> </CodeDescription>
    """

    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"
    A13 = "A13"
    A14 = "A14"
    A15 = "A15"
    A16 = "A16"
    A17 = "A17"
    A18 = "A18"
    A19 = "A19"
    A20 = "A20"
    A21 = "A21"
    A22 = "A22"
    A23 = "A23"
    A24 = "A24"
    A25 = "A25"
    A26 = "A26"
    A27 = "A27"
    A28 = "A28"
    A29 = "A29"
    A30 = "A30"
    A31 = "A31"
    A32 = "A32"
    A33 = "A33"
    A34 = "A34"
    A35 = "A35"
    A36 = "A36"
    A37 = "A37"
    A38 = "A38"
    A39 = "A39"
    A40 = "A40"
    A41 = "A41"
    A42 = "A42"
    A43 = "A43"
    A44 = "A44"
    A45 = "A45"
    A46 = "A46"


class UnitOfMeasureTypeList(Enum):
    """
    :cvar A59: <CodeDescription xmlns=""> <Title>OKTA unit</Title>
        <Definition>A unit of measurement of the cloudiness expressed in
        OKTA or OCTA, i.e. A unit of count defining the number of
        eighth-parts as a measure of the celestial dome cloud
        coverage.</Definition> </CodeDescription>
    :cvar A90: <CodeDescription xmlns=""> <Title>gigawatt</Title>
        <Definition>GW unit as per UN/CEFACT recommendation
        20.</Definition> </CodeDescription>
    :cvar A97: <CodeDescription xmlns=""> <Title>hectopascal</Title>
        <Definition>A unit of measurement of the pressure expressed in
        hectopascal.</Definition> </CodeDescription>
    :cvar AMP: <CodeDescription xmlns=""> <Title>ampere</Title>
        <Definition>The unit of electrical current in the International
        system of Units (SI) equivalent to one Coulomb per
        second.</Definition> </CodeDescription>
    :cvar C62: <CodeDescription xmlns=""> <Title>One</Title>
        <Definition>A unit for dimensionless quantities, also called
        quantities of dimension one.</Definition> </CodeDescription>
    :cvar CEL: <CodeDescription xmlns=""> <Title>Celsius</Title>
        <Definition>A unit of measurement of temperature expressed in
        degree Celsius.</Definition> </CodeDescription>
    :cvar D54: <CodeDescription xmlns=""> <Title>watt per square
        meter</Title> <Definition>A unit of measurement of the density
        of heat flow rate expressed in watt per square
        meter.</Definition> </CodeDescription>
    :cvar DD: <CodeDescription xmlns=""> <Title>degree (unit of
        angle)</Title> <Definition>A unit of measurement of angles
        expressed in a 0 to 360 degree gradient.</Definition>
        </CodeDescription>
    :cvar E08: <CodeDescription xmlns=""> <Title>Megawatt per
        Hertz</Title> <Definition>A unit of energy expressed as the load
        change in million watts that will cause a frequency shift of one
        hertz.</Definition> </CodeDescription>
    :cvar GWH: <CodeDescription xmlns=""> <Title>gigawatt hour</Title>
        <Definition>GWh unit as per UN/CEFACT recommendation
        20.</Definition> </CodeDescription>
    :cvar HMQ: <CodeDescription xmlns=""> <Title>cubic
        hectometres</Title> <Definition>A unit of volume equal to one
        million cubic metres.</Definition> </CodeDescription>
    :cvar HTZ: <CodeDescription xmlns=""> <Title>Hertz</Title>
        <Definition>HTZ unit as per UN/CEFACT recommendation
        20.</Definition> </CodeDescription>
    :cvar KEL: <CodeDescription xmlns=""> <Title>K (Kelvin)</Title>
        <Definition>Temperature unit refer ISO 80000-5 (Quantities and
        units, Part 5: Thermodynamics).</Definition> </CodeDescription>
    :cvar KMT: <CodeDescription xmlns=""> <Title>kilometre</Title>
        <Definition>km unit as per UN/CEFACT recommendation
        20.</Definition> </CodeDescription>
    :cvar KVR: <CodeDescription xmlns=""> <Title>kilovolt ampere
        reactive</Title> <Definition>A unit of electrical reactive power
        represented by a current of one thousand amperes flowing due to
        a potential difference of one thousand volts where the sine of
        the phase angle between them is 1. The unity power factor is
        expressed in thousands of a volt ampere reactive.</Definition>
        </CodeDescription>
    :cvar KVT: <CodeDescription xmlns=""> <Title>kilovolt</Title>
        <Definition>kV unit as per UN/CEFACT recommendation
        20.</Definition> </CodeDescription>
    :cvar KWH: <CodeDescription xmlns=""> <Title>kilowatt hour</Title>
        <Definition>A total amount of electrical energy transferred or
        consumed in one hour.</Definition> </CodeDescription>
    :cvar KWT: <CodeDescription xmlns=""> <Title>kilowatt</Title>
        <Definition>A unit of bulk power flow, which can be defined as
        the rate of energy transfer /consumption when a current of 1000
        amperes flows due to a potential of 1000 volts at unity power
        factor expressed in thousands of a watt.</Definition>
        </CodeDescription>
    :cvar MAH: <CodeDescription xmlns=""> <Title>megavolt ampere
        reactive hours</Title> <Definition>Total amount of reactive
        power across a power system.</Definition> </CodeDescription>
    :cvar MAR: <CodeDescription xmlns=""> <Title>megavolt ampere
        reactive</Title> <Definition>A unit of electrical reactive power
        represented by a current of one thousand amperes flowing due to
        a potential difference of one thousand volts where the sine of
        the phase angle between them is 1.</Definition>
        </CodeDescription>
    :cvar MAW: <CodeDescription xmlns=""> <Title>megawatt</Title>
        <Definition>A unit of bulk power flow, which can be defined as
        the rate of energy transfer /consumption when a current of 1000
        amperes flows due to a potential of 1000 volts at unity power
        factor expressed in millions of a watt.</Definition>
        </CodeDescription>
    :cvar MIN: <CodeDescription xmlns=""> <Title>minute</Title>
        <Definition>A period of time equal to sixty
        seconds.</Definition> </CodeDescription>
    :cvar MMT: <CodeDescription xmlns=""> <Title>millimeter</Title>
        <Definition>A unit of measurement of length expressed in
        millimeter.</Definition> </CodeDescription>
    :cvar MQS: <CodeDescription xmlns=""> <Title>cubic metres per
        second</Title> <Definition>The volume flow rate of cubic metre
        per second.</Definition> </CodeDescription>
    :cvar MTQ: <CodeDescription xmlns=""> <Title>cubic metre</Title>
        <Definition>A Cubic metre.</Definition> </CodeDescription>
    :cvar MTR: <CodeDescription xmlns=""> <Title>metre</Title>
        <Definition>The length of a metre.</Definition>
        </CodeDescription>
    :cvar MTS: <CodeDescription xmlns=""> <Title>meter per
        second</Title> <Definition>A unit of measurement of the speed
        expressed in m/s.</Definition> </CodeDescription>
    :cvar MTZ: <CodeDescription xmlns=""> <Title>millihertz</Title>
        <Definition>A unit of frequency equal to 0.001 cycle per
        second.</Definition> </CodeDescription>
    :cvar MVA: <CodeDescription xmlns=""> <Title>megavolt-ampere</Title>
        <Definition>MVA unit as per UN/CEFACT recommendation
        20.</Definition> </CodeDescription>
    :cvar MWH: <CodeDescription xmlns=""> <Title>megawatt hours</Title>
        <Definition>The total amount of bulk energy transferred or
        consumed.</Definition> </CodeDescription>
    :cvar P1: <CodeDescription xmlns=""> <Title>percent</Title>
        <Definition>A unit of proportion equal to 0.01.</Definition>
        </CodeDescription>
    :cvar SEC: <CodeDescription xmlns=""> <Title>second</Title>
        <Definition>A period of time equal to one second.</Definition>
        </CodeDescription>
    :cvar WTT: <CodeDescription xmlns=""> <Title>watt</Title>
        <Definition>The watt is the International System of Units (SI)
        standard unit of power (energy per unit time), the equivalent of
        one joule per second.</Definition> </CodeDescription>
    """

    A59 = "A59"
    A90 = "A90"
    A97 = "A97"
    AMP = "AMP"
    C62 = "C62"
    CEL = "CEL"
    D54 = "D54"
    DD = "DD"
    E08 = "E08"
    GWH = "GWH"
    HMQ = "HMQ"
    HTZ = "HTZ"
    KEL = "KEL"
    KMT = "KMT"
    KVR = "KVR"
    KVT = "KVT"
    KWH = "KWH"
    KWT = "KWT"
    MAH = "MAH"
    MAR = "MAR"
    MAW = "MAW"
    MIN = "MIN"
    MMT = "MMT"
    MQS = "MQS"
    MTQ = "MTQ"
    MTR = "MTR"
    MTS = "MTS"
    MTZ = "MTZ"
    MVA = "MVA"
    MWH = "MWH"
    P1 = "P1"
    SEC = "SEC"
    WTT = "WTT"


class UnitSymbol(Enum):
    """
    :cvar AMP: <CodeDescription xmlns=""> <Title>Ampere</Title>
        <Definition>The unit of electrical current in the International
        system of Units (SI) equivalent to one Coulomb per
        second.</Definition> </CodeDescription>
    :cvar C62: <CodeDescription xmlns=""> <Title>One</Title>
        <Definition>A unit for dimensionless quantities, also called
        quantities of dimension one.</Definition> </CodeDescription>
    :cvar DD: <CodeDescription xmlns=""> <Title>degree (unit of
        angle)</Title> <Definition>A unit of measurement of angles
        expressed in a 0 to 360 degree gradient.</Definition>
        </CodeDescription>
    :cvar GKH: <CodeDescription xmlns=""> <Title>grams per kilowatt
        hour</Title> <Definition>It represents the mass rate of
        emissions per unit of work accomplished.</Definition>
        </CodeDescription>
    :cvar HTZ: <CodeDescription xmlns=""> <Title>Hertz</Title>
        <Definition>HTZ unit as per UN/CEFACT recommendation
        20</Definition> </CodeDescription>
    :cvar KVT: <CodeDescription xmlns=""> <Title>kV</Title>
        <Definition>The symbol of kV</Definition> </CodeDescription>
    :cvar MAR: <CodeDescription xmlns=""> <Title>MVAr</Title>
        <Definition>The symbol of MVAr</Definition> </CodeDescription>
    :cvar MAW: <CodeDescription xmlns=""> <Title>MW</Title>
        <Definition>The symbol of MW</Definition> </CodeDescription>
    :cvar MVA: <CodeDescription xmlns=""> <Title>megavolt-ampere</Title>
        <Definition>MVA unit as per UN/CEFACT recommendation
        20</Definition> </CodeDescription>
    :cvar OHM: <CodeDescription xmlns=""> <Title>Ohm</Title>
        <Definition>The symbol of Ohm Unit</Definition>
        </CodeDescription>
    :cvar P1: <CodeDescription xmlns=""> <Title>Percent</Title>
        <Definition>A unit of proportion equal to 0.01.</Definition>
        </CodeDescription>
    """

    AMP = "AMP"
    C62 = "C62"
    DD = "DD"
    GKH = "GKH"
    HTZ = "HTZ"
    KVT = "KVT"
    MAR = "MAR"
    MAW = "MAW"
    MVA = "MVA"
    OHM = "OHM"
    P1 = "P1"
