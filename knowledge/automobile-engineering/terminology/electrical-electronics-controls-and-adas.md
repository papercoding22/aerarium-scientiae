# Electrical, Electronics, Controls, Software, And ADAS Terms

These terms cover vehicle electrical power, electronic control, communication networks, software, diagnostics, and driver-assistance sensors and functions.

## Table Of Contents

- [Electrical Foundations](#electrical-foundations)
- [Vehicle Electrical Hardware](#vehicle-electrical-hardware)
- [Sensors Actuators And Control](#sensors-actuators-and-control)
- [Vehicle Networks](#vehicle-networks)
- [Software And Diagnostics](#software-and-diagnostics)
- [ADAS And Automated Driving](#adas-and-automated-driving)

## Electrical Foundations

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| electric charge | điện tích | Fundamental electrical quantity carried by particles and stored in capacitive systems. | `q`; coulomb (`C`). Battery charge capacity often uses `Ah`. |
| voltage | điện áp | Electric potential difference that can drive current through a circuit. | `V` or `U`; volt (`V`). |
| current | dòng điện; cường độ dòng điện | Rate of electric-charge flow. | `I`; ampere (`A`). |
| resistance | điện trở | Opposition to direct current, relating voltage and current in an ohmic element. | `R = V/I`; ohm (`Ω`). |
| impedance | tổng trở | Frequency-dependent opposition to alternating or changing current. | `Z`; ohm (`Ω`), includes magnitude and phase. |
| capacitance | điện dung | Ability to store electric charge per unit voltage. | `C`; farad (`F`). |
| inductance | độ tự cảm | Property by which changing current produces opposing induced voltage. | `L`; henry (`H`). |
| electrical power | công suất điện | Rate of electrical-energy transfer. | DC: `P = V·I`; watt (`W`). |
| electrical energy | điện năng | Electrical power integrated over time. | joule (`J`) or watt-hour (`Wh`). |
| direct current (DC) | dòng điện một chiều | Current with a defined unidirectional average flow. | `DC`; batteries provide DC. |
| alternating current (AC) | dòng điện xoay chiều | Current that changes direction periodically. | `AC`; frequency in hertz (`Hz`). |
| ground | mass; điểm mát; nối đất tham chiếu | Reference conductor or potential used by a circuit. | Vehicle chassis is often the low-voltage return, but `ground` need not mean Earth. |
| open circuit | mạch hở | Broken or disconnected current path with very high effective resistance. | Current is near zero, though voltage may be present. |
| short circuit | ngắn mạch; chập mạch | Unintended low-resistance connection between circuit points. | Can cause excessive current or incorrect signal level. |
| voltage drop | sụt áp | Difference in voltage across a component, conductor, or connection under current. | Volt (`V`); excessive drop can reveal resistance faults. |
| power loss | tổn hao công suất | Input power not delivered as useful output, usually converted to heat. | `P_loss`; watt (`W`). |

## Vehicle Electrical Hardware

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| 12-volt battery | ắc quy 12 vôn | Low-voltage storage battery supporting starting and vehicle electrical loads. | Nominal 12 V; actual terminal voltage varies. |
| alternator | máy phát điện xoay chiều | Engine-driven generator and rectifier supplying DC electrical power and charging the battery. | Output in ampere (`A`) or kilowatt (`kW`). |
| starter motor | mô-tơ đề; máy khởi động | High-torque electric motor cranking a combustion engine for starting. | Engages flywheel or flexplate ring gear. |
| fuse | cầu chì | Overcurrent protection device that opens by melting. | Current rating in ampere (`A`); never replace with a higher value without authorization. |
| circuit breaker | bộ ngắt mạch | Resettable device opening a circuit during overcurrent or fault conditions. | Thermal, magnetic, electronic, or combined. |
| relay | rơ-le | Electrically operated switch allowing a low-power command to control another circuit. | Electromechanical or solid-state. |
| wiring harness | bó dây điện; bộ dây điện | Organized assembly of wires, connectors, terminals, protection, and branches. | Designed for current, signal integrity, environment, and assembly. |
| wire gauge | cỡ dây điện | Standard measure related to conductor cross-sectional size. | `mm²` or `AWG`; ampacity also depends on temperature and installation. |
| connector | giắc nối; đầu nối | Mating assembly making detachable electrical connections. | Includes housing, terminals, seals, locks, and keying. |
| terminal | chân điện; đầu cực | Conductive contact attached to a wire or device within a connection system. | Crimped, welded, soldered, or bolted. |
| shielding | che chắn điện từ | Conductive barrier reducing electromagnetic coupling into or out of a circuit. | Often used for high-speed data and sensitive sensors. |
| electromagnetic compatibility (EMC) | tương thích điện từ | Ability to operate correctly without causing or suffering unacceptable electromagnetic disturbance. | `EMC`; includes emissions and immunity. |
| electromagnetic interference (EMI) | nhiễu điện từ | Unwanted electromagnetic energy affecting equipment or signals. | `EMI`. |
| quiescent current | dòng điện tĩnh | Current drawn while the vehicle or module is in a defined inactive state. | Ampere or milliampere; excessive draw can discharge battery. |
| load shedding | cắt giảm phụ tải | Controlled shutdown or reduction of electrical loads when available power is limited. | Protects voltage and critical functions. |

## Sensors Actuators And Control

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| sensor | cảm biến | Device converting a physical or chemical quantity into usable information. | Defined by range, accuracy, resolution, bandwidth, and diagnostics. |
| transducer | bộ chuyển đổi; cảm biến chuyển đổi | Device converting one form of energy or physical quantity into another. | A sensor is a type of input transducer. |
| actuator | cơ cấu chấp hành | Device converting a control command and energy into physical action. | Electric, hydraulic, pneumatic, thermal, or other type. |
| electronic control unit (ECU) | bộ điều khiển điện tử | Embedded computer controlling one or more vehicle functions. | `ECU`; includes processor, memory, I/O, power supply, and software. |
| input | đầu vào; tín hiệu vào | Information or energy entering a system. | Sensor signal and driver command are inputs. |
| output | đầu ra; tín hiệu ra | Information, energy, or action produced by a system. | Actuator command is a control output. |
| analog signal | tín hiệu tương tự | Continuously varying signal representing information. | Voltage, current, resistance, or frequency. |
| digital signal | tín hiệu số | Signal represented by discrete states or encoded values. | Binary logic or communication frames. |
| sampling rate | tần số lấy mẫu | Number of measurements taken per unit time. | Samples per second or hertz (`Hz`). |
| signal conditioning | điều hòa tín hiệu | Filtering, amplifying, scaling, isolating, or converting a signal before processing. | Hardware or software. |
| calibration | hiệu chuẩn; dữ liệu hiệu chỉnh | Process of establishing measurement relation, or tuned parameter data used by control software. | Automotive software often uses `calibration` for tunable maps and constants. |
| control system | hệ thống điều khiển | Components and logic used to influence plant behaviour toward an objective. | Open-loop or closed-loop. |
| plant | đối tượng điều khiển | Physical system being controlled. | Example: engine airflow, motor torque, or vehicle yaw. |
| setpoint | giá trị đặt | Desired target value for a controlled quantity. | Also called reference or command. |
| feedback | phản hồi | Measured output information returned to a controller. | Enables correction of error and disturbance. |
| feedforward | điều khiển truyền thẳng | Control action based on command or measured disturbance before output error appears. | Often combined with feedback. |
| open-loop control | điều khiển vòng hở | Control without using measured output to correct action. | Simple but sensitive to variation. |
| closed-loop control | điều khiển vòng kín | Control using feedback to reduce difference between target and measured output. | Stability and response must be designed. |
| control error | sai lệch điều khiển | Difference between desired and measured controlled quantity. | `e = reference - output` under a common convention. |
| proportional-integral-derivative controller (PID) | bộ điều khiển PID | Controller combining action proportional to error, error integral, and error rate. | `PID`; terms may be used separately. |
| control map | bản đồ điều khiển | Lookup table providing output or parameter values across operating conditions. | One-dimensional or multidimensional. |
| state estimation | ước lượng trạng thái | Calculation of internal system variables that cannot be measured directly or reliably. | Examples: battery SoC and vehicle sideslip. |
| observer | bộ quan sát trạng thái | Mathematical estimator combining a model with measurements. | Examples: Luenberger or Kalman observer. |
| redundancy | tính dự phòng | Use of additional independent or diverse elements to tolerate faults. | Hardware, software, sensing, power, or communication redundancy. |
| fail-safe | an toàn khi lỗi | Design that moves to or maintains a defined safer state after a fault. | Safe state depends on function and hazard analysis. |
| fail-operational | tiếp tục hoạt động khi lỗi | Design able to continue required operation after specified faults. | Important where immediate shutdown would be unsafe. |
| limp-home mode | chế độ chạy giới hạn khi lỗi | Degraded mode retaining limited mobility after certain faults. | Also called limp mode; behaviour is vehicle-specific. |

## Vehicle Networks

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| in-vehicle network | mạng truyền thông trên xe | Communication system linking vehicle ECUs, sensors, actuators, and gateways. | Multiple network technologies can coexist. |
| Controller Area Network (CAN) | mạng CAN | Robust serial bus using prioritized message identifiers and differential signalling. | `CAN`; standardized by ISO 11898 family. |
| CAN frame | khung dữ liệu CAN | Structured unit transmitted on a CAN bus. | Contains identifier, control, data, and error-checking fields. |
| CAN identifier | mã định danh CAN | Arbitration and message-priority field in a CAN frame. | Describes message meaning by system convention, not a device address by itself. |
| arbitration | phân xử truy cập bus | Process allowing the highest-priority CAN frame to continue without destructive collision. | Lower numerical identifier has higher priority in classic CAN arbitration. |
| bus | đường truyền dùng chung | Shared communication medium used by multiple nodes. | Physical and protocol meaning depend on network. |
| node | nút mạng | Device connected to a communication network. | Usually an ECU, sensor, actuator, or gateway. |
| termination resistor | điện trở kết thúc đường truyền | Resistor matching bus impedance to reduce signal reflection. | High-speed CAN commonly uses 120 Ω at each physical end. |
| CAN FD | CAN tốc độ dữ liệu linh hoạt | CAN extension allowing larger payload and higher data-phase bit rate. | `CAN FD`; arbitration phase remains compatible in principle. |
| Local Interconnect Network (LIN) | mạng LIN | Low-cost single-master communication bus for simple local devices. | `LIN`; commonly slower than CAN. |
| FlexRay | mạng FlexRay | Deterministic high-speed vehicle network with time-triggered capability. | Used in some safety and chassis systems. |
| Automotive Ethernet | Ethernet ô tô | Ethernet adapted for automotive physical layers, timing, diagnostics, and environment. | Common rates include 100 Mb/s and 1 Gb/s classes. |
| gateway | bộ cổng kết nối mạng | ECU routing, filtering, translating, or securing communication between networks. | Central or zonal architecture. |
| domain controller | bộ điều khiển miền | High-capability controller combining functions within a domain such as chassis or infotainment. | Domain boundaries vary by architecture. |
| zonal controller | bộ điều khiển vùng | Controller grouping local I/O and communication by physical vehicle zone. | Reduces wiring and supports centralized computing. |
| message | thông điệp | Logical information transmitted between functions or nodes. | May be carried in one or more frames or packets. |
| signal | tín hiệu dữ liệu | Encoded data element within a network message. | Has bit position, length, scaling, offset, unit, and validity rules. |
| bit rate | tốc độ bit | Number of transmitted bits per second. | bit/s, kbit/s, or Mbit/s. Not identical to useful data throughput. |
| latency | độ trễ | Time from an event or transmission request to reception or response. | Second, millisecond, or microsecond. |

## Software And Diagnostics

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| embedded software | phần mềm nhúng | Software running inside a dedicated electronic product or ECU. | Must meet timing, memory, safety, and environmental constraints. |
| firmware | phần sụn | Low-level software closely tied to hardware and stored in non-volatile memory. | Boundary from embedded software is not universal. |
| bootloader | chương trình nạp khởi động | Software starting an ECU and supporting application validation or reprogramming. | Security and recovery are important. |
| real-time system | hệ thống thời gian thực | System whose correctness depends on both result and delivery time. | `Real-time` does not simply mean very fast. |
| task | tác vụ | Scheduled unit of software execution. | Periodic, event-driven, or background. |
| diagnostic | chẩn đoán; chức năng chẩn đoán | Function used to detect, record, communicate, or investigate faults. | Onboard and offboard diagnostics. |
| onboard diagnostics (OBD) | chẩn đoán trên xe | Standardized and manufacturer-specific vehicle self-diagnostic capability. | `OBD`; `OBD-II` is common informal US-oriented naming. |
| diagnostic link connector (DLC) | giắc chẩn đoán | Standard physical connector used to access vehicle diagnostics. | `DLC`; common road vehicles use a 16-pin form for legislated OBD. |
| diagnostic trouble code (DTC) | mã lỗi chẩn đoán | Structured code identifying a detected fault condition, not automatically its root cause. | `DTC`; examples begin with `P`, `B`, `C`, or `U`. |
| freeze-frame data | dữ liệu đóng băng tại thời điểm lỗi | Snapshot of selected operating values stored when a fault condition is detected. | Helps reproduce diagnostic context. |
| parameter identifier (PID) | mã định danh thông số | Identifier used to request or represent diagnostic data. | `PID`; standardized and manufacturer-specific forms exist. |
| scan tool | máy chẩn đoán; thiết bị quét lỗi | External tool communicating with vehicle ECUs for data, codes, tests, and programming. | Capability varies greatly. |
| live data | dữ liệu thời gian thực | Diagnostic values reported while the system operates. | Update rate may be slower than actual ECU sampling. |
| active test | kiểm tra kích hoạt | Diagnostic command operating an actuator or function to observe response. | Also called output control or bidirectional test. |
| Unified Diagnostic Services (UDS) | dịch vụ chẩn đoán hợp nhất | Application-layer diagnostic protocol defining services such as reading data and programming. | `UDS`; standardized by ISO 14229. |
| diagnostic session | phiên chẩn đoán | ECU operating mode enabling a defined set of diagnostic services. | Default, extended, and programming are common concepts. |
| reflashing | nạp lại phần mềm ECU | Reprogramming non-volatile ECU software or calibration memory. | Requires power stability, compatibility, and security authorization. |
| over-the-air update (OTA) | cập nhật qua mạng không dây | Remote delivery and installation of vehicle software or data. | `OTA`; requires secure download, validation, rollback, and lifecycle control. |
| fault detection | phát hiện lỗi | Determining that behaviour differs from an acceptable condition. | Detection is not isolation or root-cause confirmation. |
| fault isolation | khoanh vùng lỗi | Determining which component, path, or cause class is responsible for detected abnormal behaviour. | Part of diagnosis. |

## ADAS And Automated Driving

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| advanced driver-assistance system (ADAS) | hệ thống hỗ trợ lái xe nâng cao | Vehicle function assisting perception, warning, or control while responsibility remains defined by its design level. | `ADAS`; capabilities and limitations must be stated. |
| automated driving system (ADS) | hệ thống lái xe tự động | Hardware and software collectively performing the dynamic driving task within a defined operational domain. | `ADS`; terminology follows the chosen standard or regulation. |
| operational design domain (ODD) | miền thiết kế vận hành | Conditions in which an automated function is designed to operate. | `ODD`; may include roads, speed, weather, lighting, and geography. |
| dynamic driving task (DDT) | nhiệm vụ lái xe động | Real-time operational and tactical functions needed to drive a vehicle. | `DDT`; includes lateral and longitudinal control and object response. |
| radar | ra-đa | Sensor using radio waves to estimate range, relative velocity, and sometimes angle. | Frequency band and resolution depend on system. |
| lidar | lidar; cảm biến quét laser | Sensor using emitted light to measure distance and build spatial information. | `LiDAR`; architecture may be scanning or solid-state. |
| camera | camera; máy ảnh cảm biến | Optical sensor capturing image data for lanes, objects, signs, driver monitoring, and other functions. | Performance depends on lighting, optics, processing, and cleanliness. |
| ultrasonic sensor | cảm biến siêu âm | Sensor using high-frequency sound for short-range distance measurement. | Common in parking assistance. |
| inertial measurement unit (IMU) | bộ đo lường quán tính | Sensor assembly measuring acceleration and angular rate, sometimes magnetic field. | `IMU`; accelerometers and gyroscopes. |
| global navigation satellite system (GNSS) | hệ thống vệ tinh dẫn đường toàn cầu | Satellite-based position, velocity, and time service. | `GNSS`; includes GPS and other constellations. |
| sensor fusion | hợp nhất cảm biến | Combination of information from multiple sensors to improve state or environment estimation. | Central to robust perception. |
| perception | nhận thức môi trường | Processing that detects, classifies, locates, and tracks relevant road features and objects. | Includes confidence and uncertainty. |
| object detection | phát hiện đối tượng | Identifying and locating objects in sensor data. | Different from tracking and classification. |
| object tracking | theo dõi đối tượng | Estimating an object's state over time from successive observations. | May estimate position, velocity, heading, and uncertainty. |
| lane detection | phát hiện làn đường | Estimation of lane boundaries or path geometry from sensors. | Quality depends on markings and environment. |
| adaptive cruise control (ACC) | kiểm soát hành trình thích ứng | Function controlling speed and following gap to a detected target within limits. | `ACC`; driver monitoring and responsibility depend on system. |
| automatic emergency braking (AEB) | phanh khẩn cấp tự động | Function automatically braking to avoid or reduce severity of a predicted collision. | `AEB`; performance depends on scenario and ODD. |
| forward collision warning (FCW) | cảnh báo va chạm phía trước | Function warning the driver of a predicted frontal collision risk. | `FCW`; does not necessarily brake. |
| lane-departure warning (LDW) | cảnh báo lệch làn | Function warning when unintended lane departure is detected. | `LDW`. |
| lane-keeping assistance (LKA) | hỗ trợ giữ làn | Function applying steering or other control to help remain within a lane. | `LKA`; not the same as full automated lane centering. |
| blind-spot monitoring (BSM) | giám sát điểm mù | Function detecting relevant vehicles or objects in side-rear blind areas. | `BSM`; sensor coverage and warning logic vary. |
| driver-monitoring system (DMS) | hệ thống giám sát người lái | System estimating driver attention, state, or availability. | `DMS`; may use camera and steering behaviour. |
| time to collision (TTC) | thời gian tới va chạm | Predicted time until collision if current relative motion continues under a chosen model. | `TTC`; second (`s`). Model assumptions matter. |
| headway | khoảng thời gian bám xe | Time gap between vehicles passing the same reference point. | Second (`s`); distinct from physical distance gap. |
| fallback | phương án xử lý dự phòng | Response taken when an automated function cannot continue normal operation. | May be performed by driver or system, depending on design. |

[Back to terminology index](README.md)
