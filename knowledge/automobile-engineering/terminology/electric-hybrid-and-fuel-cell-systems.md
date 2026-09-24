# Electric, Hybrid, And Fuel-Cell System Terms

These terms cover high-voltage batteries, electric propulsion, charging, hybrid architectures, and hydrogen fuel cells.

## Table Of Contents

- [Vehicle Types And Architectures](#vehicle-types-and-architectures)
- [Battery Cells And Packs](#battery-cells-and-packs)
- [Power Electronics And Motors](#power-electronics-and-motors)
- [Charging](#charging)
- [Safety And Thermal Management](#safety-and-thermal-management)
- [Fuel Cells](#fuel-cells)

## Vehicle Types And Architectures

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| electric vehicle (EV) | xe điện | Vehicle using one or more electric machines for propulsion. | `EV` can be broad; check whether the source means battery EV only. |
| battery-electric vehicle (BEV) | xe thuần điện | Vehicle propelled only by electrical energy stored in a rechargeable traction battery. | `BEV`; no combustion engine for propulsion. |
| hybrid electric vehicle (HEV) | xe điện lai; xe hybrid | Vehicle combining a combustion engine with electric propulsion and onboard energy recovery. | `HEV`; normally not charged from the grid. |
| plug-in hybrid electric vehicle (PHEV) | xe hybrid sạc ngoài | Hybrid with a traction battery that can be charged from an external source. | `PHEV`. |
| mild hybrid electric vehicle (MHEV) | xe hybrid nhẹ | Hybrid in which the electric system assists but normally cannot propel the vehicle alone for normal driving. | `MHEV`; often 48 V, but voltage does not define it alone. |
| fuel-cell electric vehicle (FCEV) | xe điện pin nhiên liệu | Electric vehicle using a fuel-cell system as a main onboard electrical-energy source. | `FCEV`; commonly stores compressed hydrogen. |
| series hybrid | hybrid nối tiếp | Architecture in which the combustion engine drives a generator and propulsion is provided electrically. | Mechanical engine-to-wheel path is absent in the pure definition. |
| parallel hybrid | hybrid song song | Architecture in which engine and electric machine can both provide mechanical propulsion torque. | Many layouts are possible. |
| series-parallel hybrid | hybrid nối tiếp–song song | Architecture able to combine series and parallel power paths. | Also called power-split hybrid in some designs. |
| power-split device | bộ phân chia công suất | Mechanism dividing or combining mechanical power paths in some hybrid systems. | Often uses a planetary gearset. |
| traction battery | pin kéo; bộ pin động lực | Rechargeable battery supplying high power and energy for vehicle propulsion. | Usually high voltage in BEVs and full hybrids. |
| traction motor | động cơ điện kéo | Electric machine producing propulsion torque. | May also operate as a generator. |
| electric drive unit (EDU) | cụm truyền động điện | Integrated assembly containing motor, power electronics, and reduction gearing in some vehicles. | `EDU`; manufacturer boundaries vary. |
| regenerative braking | phanh tái sinh | Deceleration in which an electric machine converts vehicle kinetic energy into electrical energy. | Limited by battery acceptance, motor capacity, grip, and stability needs. |
| blended braking | phanh phối hợp | Coordinated use of regenerative and friction braking to meet driver demand. | Control must preserve pedal feel and stability. |

## Battery Cells And Packs

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| electrochemical cell | tế bào điện hóa; cell pin | Smallest battery unit that converts chemical energy to electrical energy. | One cell has a characteristic voltage range. |
| battery module | mô-đun pin | Mechanical and electrical group of cells forming a service or manufacturing unit. | Module use is architecture-dependent. |
| battery pack | bộ pin | Complete battery assembly with cells, structure, connections, sensing, protection, and thermal systems. | Pack is the vehicle-level energy-storage unit. |
| anode | điện cực âm khi pin phóng điện | Electrode where oxidation occurs. | In rechargeable-cell discussions, naming is normally based on discharge. |
| cathode | điện cực dương khi pin phóng điện | Electrode where reduction occurs. | Cell chemistry is often named by cathode material. |
| electrolyte | chất điện phân | Ion-conducting medium between electrodes. | May be liquid, gel, polymer, or solid. |
| separator | màng ngăn | Porous electrical insulator preventing direct electrode contact while allowing ion movement. | Damage can contribute to internal short circuit. |
| state of charge (SoC) | trạng thái sạc; phần trăm dung lượng còn lại | Estimated available charge relative to a defined usable capacity. | `SoC`; percent. It is estimated, not directly measured. |
| state of health (SoH) | trạng thái sức khỏe pin | Estimate of battery capability compared with a defined new condition. | `SoH`; percent. May refer to capacity, resistance, power, or combined metrics. |
| battery capacity | dung lượng pin | Amount of electric charge a battery can deliver under stated conditions. | `Q`; ampere-hour (`Ah`). Energy capacity is different. |
| energy capacity | dung lượng năng lượng | Electrical energy a battery can store or deliver under stated conditions. | watt-hour (`Wh`) or kilowatt-hour (`kWh`). |
| nominal voltage | điện áp danh định | Representative voltage used to identify or calculate a battery system. | `V`; not the exact operating voltage. |
| open-circuit voltage (OCV) | điện áp hở mạch | Terminal voltage when no current flows after specified stabilization. | `OCV`; volt (`V`). Related to SoC and temperature. |
| terminal voltage | điện áp đầu cực | Voltage measured across battery terminals during rest, charge, or discharge. | `V`; changes with current, SoC, temperature, and ageing. |
| internal resistance | điện trở trong | Equivalent opposition inside a cell or pack that causes voltage drop and heat. | `R`; ohm (`Ω`). Depends on method, SoC, temperature, and frequency. |
| C-rate | tốc độ sạc/xả theo dung lượng | Charge or discharge current normalized by rated capacity. | `1C` ideally corresponds to one-hour charge or discharge at the stated capacity. |
| depth of discharge (DoD) | độ sâu xả | Portion of battery capacity removed relative to a defined full condition. | `DoD`; percent. Approximately complementary to SoC under matching definitions. |
| usable energy | năng lượng khả dụng | Energy window the vehicle allows between control limits. | `kWh`; smaller than gross energy in many packs. |
| gross energy | tổng năng lượng danh nghĩa | Total energy associated with the full specified cell or pack range. | `kWh`; definition varies by manufacturer. |
| energy density | mật độ năng lượng | Stored energy per unit mass or volume. | `Wh/kg` or `Wh/L`. |
| power density | mật độ công suất | Deliverable power per unit mass or volume. | `W/kg` or `W/L`. |
| cycle life | tuổi thọ chu kỳ | Number of specified charge-discharge cycles before reaching an end criterion. | Test window, temperature, rate, and end criterion must be stated. |
| calendar ageing | lão hóa theo thời gian | Battery degradation that occurs with time, including when not cycling. | Strongly affected by temperature and SoC. |
| cycle ageing | lão hóa do chu kỳ | Battery degradation caused by charge-discharge operation. | Depends on DoD, rate, temperature, and chemistry. |
| cell balancing | cân bằng cell pin | Control that reduces differences in cell state of charge or voltage. | Passive balancing dissipates energy; active balancing transfers it. |
| battery management system (BMS) | hệ thống quản lý pin | Electronic system estimating battery state and controlling safe pack operation. | `BMS`; monitors voltage, current, temperature, isolation, and limits. |

## Power Electronics And Motors

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| electric machine | máy điện | Device converting electrical and mechanical energy in either direction. | Can operate as motor or generator. |
| motor mode | chế độ động cơ | Operation converting electrical power into mechanical power. | Produces torque. |
| generator mode | chế độ máy phát | Operation converting mechanical power into electrical power. | Used during regeneration or engine generation. |
| stator | stato; phần tĩnh | Stationary electromagnetic part of an electric machine. | Often contains windings. |
| rotor | rôto; phần quay | Rotating electromagnetic part of an electric machine. | May use magnets, conductors, or reluctance geometry. |
| permanent-magnet synchronous motor (PMSM) | động cơ đồng bộ nam châm vĩnh cửu | AC machine whose permanent-magnet rotor rotates synchronously with the stator field. | `PMSM`; common in EV traction. |
| induction motor | động cơ không đồng bộ; động cơ cảm ứng | AC machine in which rotor current is induced by the stator field. | Rotor speed differs from synchronous speed by slip. |
| switched-reluctance motor (SRM) | động cơ từ trở chuyển mạch | Machine producing torque as a salient rotor moves toward lower magnetic reluctance. | `SRM`; requires electronic commutation. |
| motor torque | mô-men động cơ điện | Torque produced or absorbed by an electric machine. | `T`; `N·m`. Positive sign convention must be defined. |
| base speed | tốc độ cơ sở | Speed below which a motor can often provide approximately constant maximum torque. | Above it, voltage limits usually require field weakening. |
| field weakening | suy yếu từ trường | Control used to operate an electric machine above base speed by reducing effective flux. | Extends speed range with declining torque capability. |
| inverter | bộ nghịch lưu | Power-electronic converter between DC battery power and controlled AC machine power. | Uses semiconductor switches and pulse-width modulation. |
| rectifier | bộ chỉnh lưu | Converter changing alternating current to direct current. | Can be passive or actively controlled. |
| DC-DC converter | bộ biến đổi một chiều–một chiều | Power converter changing one DC voltage level to another. | Often supplies the 12 V network from the high-voltage bus. |
| onboard charger (OBC) | bộ sạc tích hợp trên xe | Vehicle-mounted converter that changes external AC power into controlled DC battery charging power. | `OBC`; charging power in `kW`. |
| power semiconductor | linh kiện bán dẫn công suất | Electronic switch or diode controlling high voltage and current. | Examples: `IGBT`, silicon `MOSFET`, silicon-carbide `MOSFET`. |
| pulse-width modulation (PWM) | điều chế độ rộng xung | Control method varying average voltage or current through switched pulse duration. | `PWM`; switching frequency in hertz (`Hz`). |
| resolver | cảm biến vị trí rôto kiểu resolver | Rotary electromagnetic sensor measuring shaft angle. | Common in traction motors for robust position feedback. |
| reduction gear | bộ giảm tốc | Fixed or variable gearing reducing motor speed and multiplying torque. | Most BEVs use a single-speed fixed reduction. |
| inverter efficiency | hiệu suất bộ nghịch lưu | Ratio of inverter output power to input power under a stated direction and condition. | Percent; varies with voltage, current, switching, and temperature. |

## Charging

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| charging | quá trình sạc | Controlled transfer of electrical energy into a rechargeable battery. | Defined by voltage, current, power, temperature, and limits. |
| AC charging | sạc xoay chiều | Charging where AC enters the vehicle and the onboard charger converts it to DC. | Power limited by supply, cable, and OBC. |
| DC fast charging | sạc nhanh một chiều | Charging where external equipment supplies controlled DC to the traction battery. | Vehicle OBC is bypassed for traction-battery power conversion. |
| charge port | cổng sạc | Vehicle inlet and interface for connecting charging equipment. | Connector type varies by region and vehicle. |
| electric vehicle supply equipment (EVSE) | thiết bị cấp điện cho xe điện | Equipment providing controlled and protected electrical connection to an EV. | `EVSE`; not always the charger itself. |
| charging station | trạm sạc | Installed location or equipment offering one or more charging points. | Power rating and connector support vary. |
| charging power | công suất sạc | Rate at which electrical energy is transferred during charging. | `P`; kilowatt (`kW`). Battery power may differ from grid input. |
| charging curve | đường cong công suất sạc | Charging power or current plotted against time, SoC, voltage, or another variable. | Fast-charge power normally changes through the session. |
| constant-current charging (CC) | sạc dòng điện không đổi | Charging phase controlled to a target current. | `CC`. Actual current may be reduced by limits. |
| constant-voltage charging (CV) | sạc điện áp không đổi | Charging phase controlled to a maximum target voltage while current falls. | `CV`; common near high SoC for lithium-ion cells. |
| charging efficiency | hiệu suất sạc | Ratio of energy stored or delivered by the battery to electrical energy supplied, under a stated boundary. | Percent; boundary must include or exclude auxiliaries explicitly. |
| vehicle-to-grid (V2G) | xe cấp điện ngược lên lưới | Bidirectional energy transfer from vehicle battery to electrical grid. | `V2G`; requires compatible vehicle, charger, communication, and market rules. |
| vehicle-to-load (V2L) | xe cấp điện cho tải | Use of vehicle energy to power external electrical loads. | `V2L`; output voltage and power are specified. |

## Safety And Thermal Management

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| high voltage (HV) | điện áp cao | Vehicle voltage class requiring special insulation, isolation, identification, and service procedures. | `HV`; regulatory thresholds vary. Never infer safety from voltage name alone. |
| low voltage (LV) | điện áp thấp | Vehicle electrical network below the relevant high-voltage threshold. | `LV`; often 12 V or 48 V nominal. |
| contactor | công tắc tơ | Electrically controlled high-current switch connecting or isolating a battery pack. | Main positive and negative contactors are common. |
| pre-charge circuit | mạch nạp trước | Circuit charging downstream capacitors gradually before main contactors close. | Limits inrush current. |
| service disconnect | bộ ngắt điện bảo dưỡng | Manual device that separates part of the high-voltage battery circuit for service. | Procedure and PPE remain vehicle-specific. |
| high-voltage interlock loop (HVIL) | mạch liên động điện áp cao | Low-energy monitoring loop detecting opened HV connectors or covers. | `HVIL`; can trigger controlled HV isolation. |
| isolation resistance | điện trở cách điện | Resistance between high-voltage conductors and vehicle chassis or exposed conductive parts. | Ohm (`Ω`), often normalized as `Ω/V` in requirements. |
| insulation monitoring device (IMD) | thiết bị giám sát cách điện | Device monitoring electrical isolation between HV system and chassis. | `IMD`. |
| thermal runaway | mất kiểm soát nhiệt | Self-accelerating heat-generating failure that can spread within a cell and possibly to nearby cells. | A safety event, not normal battery warming. |
| thermal propagation | lan truyền nhiệt | Spread of a cell thermal event to neighbouring cells or modules. | Pack design aims to prevent or delay propagation. |
| battery thermal management system (BTMS) | hệ thống quản lý nhiệt pin | System controlling battery temperature and temperature uniformity. | `BTMS`; air, liquid, refrigerant, or other methods. |
| cold plate | tấm làm mát | Plate with thermal paths or fluid channels used to cool or heat cells and electronics. | Interface resistance affects performance. |
| heat pump | bơm nhiệt | Refrigeration system operated to move heat for efficient cabin or battery heating. | Coefficient of performance changes with conditions. |

## Fuel Cells

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| fuel cell | pin nhiên liệu | Electrochemical device converting fuel and oxidant chemical energy directly into electrical energy. | Does not store energy like a rechargeable battery. |
| fuel-cell stack | cụm pin nhiên liệu | Series assembly of individual fuel cells producing useful voltage and power. | Stack power in kilowatt (`kW`). |
| proton-exchange membrane fuel cell (PEMFC) | pin nhiên liệu màng trao đổi proton | Low-temperature fuel-cell type commonly considered for road vehicles. | `PEMFC`; uses hydrogen and oxygen-containing air. |
| hydrogen storage tank | bình chứa hydro | Pressure vessel storing hydrogen onboard a vehicle. | Storage pressure and certification are vehicle-specific. |
| anode loop | vòng tuần hoàn anốt; vòng cực âm | Fuel-cell subsystem delivering and often recirculating hydrogen at the anode. | Water and inert-gas management are important. |
| cathode air system | hệ thống cấp khí catốt; hệ thống khí cực dương | Compressor and flow system supplying air to the fuel-cell cathode. | Compressor power is a major auxiliary load. |
| balance of plant | hệ thống phụ trợ pin nhiên liệu | Pumps, compressor, valves, humidification, cooling, sensing, and control supporting the stack. | `BoP`; boundary must be defined. |
| fuel-cell efficiency | hiệu suất pin nhiên liệu | Electrical energy output divided by fuel chemical energy input under a stated heating-value basis. | Percent; state lower or higher heating value basis. |

[Back to terminology index](README.md)
