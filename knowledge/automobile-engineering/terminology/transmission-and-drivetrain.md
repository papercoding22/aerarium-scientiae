# Transmission And Drivetrain Terms

These terms describe how torque is changed, transferred, divided, and delivered to the driven wheels.

## Table Of Contents

- [Core Quantities](#core-quantities)
- [Transmission Types](#transmission-types)
- [Transmission Components](#transmission-components)
- [Driveline Components](#driveline-components)
- [Differentials And Drive Layouts](#differentials-and-drive-layouts)

## Core Quantities

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| gear | bánh răng; cấp số | Toothed component transmitting rotary motion and torque, or a selected ratio in a transmission. | Context distinguishes physical gear from operating gear. |
| gear ratio | tỷ số truyền bánh răng | Ratio between input and output rotational speed under a stated convention. | Often `i = n_in/n_out`; always confirm convention. |
| speed reduction | giảm tốc | Gearing arrangement that lowers output speed and increases torque, apart from losses. | Reduction ratio greater than one under common input/output convention. |
| overdrive | số truyền tăng | Ratio in which transmission output rotates faster than input. | Ratio below one under common `n_in/n_out` convention. |
| final-drive ratio | tỷ số truyền lực cuối | Fixed ratio between transmission output and driven axle or differential output path. | Multiplies overall ratio. |
| overall ratio | tỷ số truyền toàn bộ | Combined ratio from engine or motor to wheel. | Product of active stage ratios under a consistent convention. |
| wheel torque | mô-men tại bánh xe | Propulsion or braking torque acting at a wheel. | `N·m`; related to tire force through effective radius. |
| driveline efficiency | hiệu suất hệ truyền lực | Output power divided by input power across a defined driveline boundary. | Percent; changes with torque, speed, temperature, and gear. |
| torque multiplication | nhân mô-men | Increase in output torque through gearing or hydrodynamic action. | Does not create energy; speed falls or another energy path supplies it. |
| shift schedule | quy luật chuyển số | Control map deciding when an automatic transmission changes ratio. | Often depends on speed, demand, load, temperature, and drive mode. |
| shift quality | chất lượng chuyển số | Objective and subjective behaviour during a ratio change. | Includes time, jerk, flare, tie-up, noise, and feel. |
| driveline lash | độ rơ hệ truyền lực | Free movement caused by clearances between driveline components. | Can cause clunk or response delay during torque reversal. |
| backlash | khe hở ăn khớp bánh răng | Clearance between mating gear tooth flanks. | Required for lubrication and thermal expansion; excessive value causes noise and impact. |

## Transmission Types

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| transmission | hộp số; bộ truyền động | Assembly selecting or creating ratios between a prime mover and driveline. | In US usage often means gearbox assembly. |
| gearbox | hộp số | Gear-based mechanism providing one or more speed and torque ratios. | Common British and general engineering term. |
| manual transmission (MT) | hộp số sàn; hộp số tay | Transmission in which the driver selects gears and normally operates a clutch. | `MT`. |
| automatic transmission (AT) | hộp số tự động | Transmission selecting ratios automatically, often using planetary gears and hydraulic clutches. | `AT`; many designs exist. |
| automated manual transmission (AMT) | hộp số sàn tự động hóa | Manual-type gearbox with automated clutch and gear selection. | `AMT`; different from torque-converter AT. |
| dual-clutch transmission (DCT) | hộp số ly hợp kép | Automated transmission using two clutches for alternating gear paths. | `DCT`; wet or dry clutches. |
| continuously variable transmission (CVT) | hộp số vô cấp | Transmission varying ratio continuously over a designed range rather than fixed steps. | `CVT`; belt, chain, toroidal, or electrical power-split forms. |
| e-CVT | hộp số vô cấp điện tử | Marketing or engineering term often used for power-split hybrid ratio control. | May not contain a belt CVT; inspect architecture. |
| transaxle | cụm hộp số–vi sai | Integrated assembly combining transmission and final drive or differential. | Common in front-wheel-drive and electric drive units. |
| single-speed reducer | bộ giảm tốc một cấp | Fixed-ratio gear reduction, common between EV motor and differential. | No multi-speed shifting in normal operation. |
| transfer case | hộp phân phối | Assembly distributing driveline torque to front and rear axles. | Common in AWD and 4WD layouts. |

## Transmission Components

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| clutch | ly hợp; côn | Friction or positive-engagement device connecting and disconnecting rotating power paths. | Torque capacity depends on clamp force, friction, and effective radius. |
| clutch disc | đĩa ly hợp; lá côn | Friction disc clamped between flywheel and pressure plate in many manual systems. | Contains hub and often torsional springs. |
| pressure plate | mâm ép; bàn ép ly hợp | Spring-loaded assembly applying clamp force to a clutch disc. | Bolted to the flywheel in common designs. |
| release bearing | bi tê; vòng bi nhả ly hợp | Bearing transferring clutch-release force to rotating clutch parts. | Also called throw-out bearing. |
| clutch pack | bộ lá ly hợp | Stack of alternating friction and steel plates transmitting torque when compressed. | Used in automatic, DCT, differential, and AWD systems. |
| wet clutch | ly hợp ướt | Clutch operating in oil for cooling and controlled friction. | Higher thermal capacity but includes fluid drag. |
| dry clutch | ly hợp khô | Clutch operating without an oil bath at its friction interface. | Lower drag but different thermal limits. |
| torque converter | bộ biến mô thủy lực | Hydrodynamic device transferring torque through fluid between engine and automatic transmission. | Contains pump, turbine, and stator. |
| lock-up clutch | ly hợp khóa biến mô | Clutch mechanically connecting torque-converter input and output to reduce slip. | Controlled for efficiency and vibration. |
| planetary gearset | bộ truyền bánh răng hành tinh | Gearset with sun gear, planet gears and carrier, and ring gear. | Ratios depend on which member is input, output, or held. |
| sun gear | bánh răng mặt trời | Central gear of a planetary gearset. | Meshes with planet gears. |
| planet gear | bánh răng hành tinh | Gear rotating on a carrier while meshing with sun and ring gears. | Also called pinion in this context. |
| planet carrier | giá mang bánh răng hành tinh | Member supporting planet-gear shafts. | Can be input, output, or reaction member. |
| ring gear | vành răng; bánh răng bao | Outer internally toothed member of a planetary gearset. | Also called annulus. |
| synchronizer | bộ đồng tốc | Mechanism matching shaft and gear speed before positive engagement in a manual gearbox. | Uses friction cones and a sleeve. |
| dog clutch | khớp răng gài | Positive-engagement clutch using interlocking teeth rather than friction surfaces. | Requires suitable speed matching. |
| shift fork | càng gạt số | Fork moving a synchronizer sleeve or dog clutch to select a gear. | Actuated manually or automatically. |
| selector mechanism | cơ cấu chọn số | Linkage or actuator system choosing a transmission operating position or gear. | Mechanical, hydraulic, or electronic. |
| input shaft | trục sơ cấp; trục vào | Transmission shaft receiving torque from the engine, motor, or clutch. | Rotational speed in `rpm`. |
| output shaft | trục thứ cấp; trục ra | Transmission shaft delivering torque to the final drive or driveline. | Boundary varies by design. |
| countershaft | trục trung gian | Shaft carrying gears between input and output paths in a gearbox. | Also called layshaft. |
| transmission control unit (TCU) | bộ điều khiển hộp số | ECU controlling transmission actuators, pressure, clutches, and shifts. | `TCU`; may be integrated into a powertrain controller. |
| valve body | thân van thủy lực | Hydraulic control assembly directing pressurized fluid in an automatic transmission. | Contains passages, valves, and often solenoids. |
| shift solenoid | van điện từ chuyển số | Electrically controlled hydraulic valve used to command transmission states. | Controlled by a TCU. |
| transmission fluid | dầu hộp số | Fluid providing lubrication, cooling, hydraulic operation, and friction behaviour. | `ATF`, gear oil, DCT fluid, and CVT fluid are not interchangeable by default. |

## Driveline Components

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| drivetrain | hệ thống truyền động; hệ thống truyền lực | Components carrying propulsion torque from a power source output to driven wheels. | Boundary may or may not include transmission. State it. |
| driveline | chuỗi truyền lực | Mechanical torque path from transmission or power unit to driven wheels. | Often used similarly to drivetrain. |
| propeller shaft | trục các-đăng | Longitudinal shaft transmitting torque between separated driveline assemblies. | Also called driveshaft in many contexts. |
| driveshaft | trục truyền động | Shaft transmitting drive torque. | May mean propeller shaft or half shaft depending on region and context. |
| universal joint (U-joint) | khớp các-đăng | Joint transmitting rotation between shafts at an angle. | Basic single joint produces speed variation at an angle. |
| constant-velocity joint (CV joint) | khớp đồng tốc | Joint transmitting rotation through an angle while maintaining nearly constant output speed. | `CV joint`; common on driven and steered wheels. |
| half shaft | bán trục | Shaft connecting a differential output to one driven wheel. | Often includes inner and outer CV joints. |
| axle | trục; cầu xe | Shaft or assembly supporting wheels, transmitting torque, or both. | Meaning varies: axle shaft, beam axle, or whole axle assembly. |
| live axle | cầu chủ động; cầu sống | Axle assembly that supports wheels and transmits propulsion torque. | Often a solid beam with differential housing. |
| dead axle | cầu bị động | Axle supporting wheels without transmitting propulsion torque. | May still carry braking loads. |
| wheel hub | moay-ơ bánh xe | Rotating wheel-mounting component supported by bearings. | Provides bolt or stud mounting pattern. |
| wheel bearing | vòng bi bánh xe | Bearing supporting wheel and hub loads while allowing rotation. | Carries radial, axial, and moment loads. |
| torsional compliance | độ mềm xoắn | Angular deflection of a driveline component under torque. | Inverse concept of torsional stiffness. |
| torsional stiffness | độ cứng xoắn | Torque required per unit angular twist. | `N·m/rad`. |

## Differentials And Drive Layouts

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| differential | bộ vi sai | Gear mechanism allowing connected outputs to rotate at different speeds while dividing torque. | Standard open differential sends equal ideal gear torque to both outputs. |
| final drive | truyền lực cuối | Last reduction stage before torque reaches axle shafts or wheels. | Often integrated with the differential. |
| differential carrier | vỏ vi sai; giá vi sai | Rotating housing supporting differential gears and receiving ring-gear torque. | Do not confuse with axle housing. |
| side gear | bánh răng bán trục | Differential gear connected to an axle or output shaft. | Meshes with pinion or spider gears. |
| spider gear | bánh răng hành tinh vi sai | Small differential gear allowing relative speed between side gears. | Also called differential pinion gear. |
| open differential | vi sai mở | Basic differential permitting wheel-speed difference without active or friction-based torque bias. | Available wheel torque is limited by low-traction side in many conditions. |
| limited-slip differential (LSD) | vi sai hạn chế trượt | Differential that resists excessive output-speed difference or biases torque. | `LSD`; clutch, helical, viscous, or controlled types. |
| locking differential | khóa vi sai; vi sai khóa | Differential capable of forcing its outputs to rotate together. | Useful for traction; affects turning behaviour. |
| torque-biasing differential | vi sai phân bổ mô-men | Differential using internal mechanics to produce a torque ratio between outputs. | Bias ratio depends on design and operating state. |
| electronically controlled differential | vi sai điều khiển điện tử | Differential whose clutch or actuator is controlled electronically. | Often called `e-diff`, but that name may also mean brake-based control. |
| center differential | vi sai trung tâm | Differential allowing front and rear axle speed difference in some AWD systems. | Can be open, limited-slip, lockable, or actively controlled. |
| torque vectoring | phân bổ mô-men chủ động | Controlled variation of drive or brake torque among wheels to influence traction and yaw. | Can use differentials, motors, or brakes. |
| front-wheel drive (FWD) | dẫn động cầu trước | Drive layout sending propulsion torque to front wheels. | `FWD`. |
| rear-wheel drive (RWD) | dẫn động cầu sau | Drive layout sending propulsion torque to rear wheels. | `RWD`. |
| all-wheel drive (AWD) | dẫn động tất cả các bánh | System capable of driving front and rear axles, continuously or on demand. | `AWD`; not one fixed architecture. |
| four-wheel drive (4WD) | dẫn động bốn bánh | Term often used for selectable, lockable, or off-road-oriented four-wheel drive. | `4WD`; difference from AWD is convention, not a universal law. |
| part-time four-wheel drive | dẫn động bốn bánh bán thời gian | System where the driver or controller engages the second axle and may lack a center differential. | Locked use on high-grip roads can cause driveline wind-up. |
| full-time four-wheel drive | dẫn động bốn bánh toàn thời gian | System permitting four-wheel drive on normal surfaces, usually with center speed differentiation. | May include a lock mode. |
| driveline wind-up | ứng suất tích tụ trong hệ truyền lực | Torsional stress caused when connected axles require different path speeds but cannot differentiate. | Can cause tire scrub, binding, and component load. |

[Back to terminology index](README.md)
