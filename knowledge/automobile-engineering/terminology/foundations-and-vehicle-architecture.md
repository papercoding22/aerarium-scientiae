# Foundations And Vehicle Architecture Terms

Use these terms to describe physical quantities, the basic shape of a vehicle, and its overall performance.

## Table Of Contents

- [Measurement And Mechanics](#measurement-and-mechanics)
- [Heat And Fluids](#heat-and-fluids)
- [Vehicle Architecture](#vehicle-architecture)
- [Aerodynamics And Performance](#aerodynamics-and-performance)
- [Noise And Vibration](#noise-and-vibration)

## Measurement And Mechanics

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| quantity | đại lượng | A property that can be measured and expressed with a value and unit. | Examples: length, mass, time, force. |
| scalar | đại lượng vô hướng | A quantity with magnitude but no direction. | Examples: mass, temperature, energy. |
| vector | đại lượng vectơ | A quantity with both magnitude and direction. | Examples: force, velocity, acceleration. |
| dimension | thứ nguyên | The physical nature of a quantity, independent of the chosen unit. | Force has dimensions `M·L·T⁻²`. |
| unit | đơn vị | An agreed reference used to express a measured quantity. | SI examples: `m`, `kg`, `s`, `N`. |
| tolerance | dung sai | The permitted variation from a specified dimension or value. | Often written as a range or `±` value. |
| accuracy | độ chính xác | How close a measured value is to the true or accepted value. | Different from precision. |
| precision | độ chụm; độ lặp lại | How closely repeated measurements agree with each other. | High precision does not guarantee accuracy. |
| resolution | độ phân giải | The smallest change an instrument or system can distinguish. | Depends on the sensor and measurement system. |
| uncertainty | độ không đảm bảo đo | A quantified range expressing doubt about a measurement result. | Reported with a confidence level or coverage factor. |
| length | chiều dài | Distance measured along one dimension. | `l`; metre (`m`). |
| area | diện tích | Size of a two-dimensional surface. | `A`; square metre (`m²`). |
| volume | thể tích | Space occupied by a three-dimensional object or fluid. | `V`; cubic metre (`m³`), litre (`L`). |
| mass | khối lượng | The amount of matter and a measure of resistance to acceleration. | `m`; kilogram (`kg`). |
| weight | trọng lượng | The gravitational force acting on a mass. | `W = m·g`; newton (`N`), not `kg`. |
| density | khối lượng riêng | Mass per unit volume. | `ρ = m/V`; `kg/m³`. |
| time | thời gian | Duration between events. | `t`; second (`s`). |
| displacement | độ dịch chuyển | Change in position from a starting point to an ending point. | Vector; metre (`m`). Also means engine swept volume in engine context. |
| distance | quãng đường | Total path length travelled. | Scalar; metre (`m`) or kilometre (`km`). |
| speed | tốc độ | Rate at which distance changes. | `v`; `m/s` or `km/h`. |
| velocity | vận tốc | Rate of position change with direction. | Vector `v`; `m/s`. |
| acceleration | gia tốc | Rate at which velocity changes. | `a`; `m/s²`. |
| angular velocity | vận tốc góc | Rate of rotation about an axis. | `ω`; `rad/s`. Revolutions per minute (`rpm`) is common but non-SI. |
| force | lực | An interaction that can accelerate or deform an object. | `F = m·a`; newton (`N`). |
| moment | mô-men lực | Turning effect of a force about a point or axis. | `M`; newton metre (`N·m`). |
| torque | mô-men xoắn | A moment transmitted about a rotating shaft or axis. | `T` or `τ`; `N·m`. |
| work | công | Energy transferred when a force acts through a displacement. | `W`; joule (`J`). |
| energy | năng lượng | Capacity to perform work or cause change. | `E`; joule (`J`), watt-hour (`Wh`). |
| power | công suất | Rate of doing work or transferring energy. | `P = dE/dt`; watt (`W`) or kilowatt (`kW`). |
| horsepower | mã lực | A non-SI unit of power used for engines and motors. | Metric `PS` and mechanical `hp` are not exactly equal. |
| momentum | động lượng | Product of mass and velocity. | `p = m·v`; `kg·m/s`. |
| inertia | quán tính | Tendency of an object to resist a change in motion. | Translational inertia relates to mass. |
| mass moment of inertia | mô-men quán tính khối lượng | Resistance of a body to angular acceleration about an axis. | `I`; `kg·m²`. |
| friction | ma sát | Resistance to relative motion between contacting surfaces. | Friction force commonly depends on normal load and coefficient. |
| coefficient of friction | hệ số ma sát | Ratio used to relate friction force to normal force in a simplified model. | `μ`; dimensionless. Static and kinetic values differ. |
| normal force | phản lực pháp tuyến | Contact force perpendicular to a surface. | `N`; newton (`N`). Do not confuse symbol `N` with the unit newton. |
| stress | ứng suất | Internal force divided by area inside a material. | `σ` or `τ`; pascal (`Pa`). |
| strain | biến dạng tương đối | Change in dimension divided by original dimension. | `ε`; dimensionless. |
| stiffness | độ cứng | Resistance to deformation under load. | Linear stiffness `k`; `N/m`. Different from material hardness. |
| damping | giảm chấn; cản dao động | Removal or dissipation of vibration energy. | Viscous damping coefficient `c`; `N·s/m`. |
| natural frequency | tần số riêng | Frequency at which a system tends to vibrate when disturbed. | `fₙ`; hertz (`Hz`). |
| resonance | cộng hưởng | Large response that can occur when excitation is near a natural frequency. | Engineers avoid harmful resonance or control it with damping. |

## Heat And Fluids

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| temperature | nhiệt độ | A measure related to the thermal state of matter. | `T`; kelvin (`K`) or degree Celsius (`°C`). |
| heat | nhiệt lượng; nhiệt | Energy transferred because of a temperature difference. | `Q`; joule (`J`). Heat is not the same as temperature. |
| heat transfer | truyền nhiệt | Movement of thermal energy by conduction, convection, or radiation. | Heat-transfer rate often uses watt (`W`). |
| thermal conductivity | độ dẫn nhiệt | Ability of a material to conduct heat. | `k`; `W/(m·K)`. |
| specific heat capacity | nhiệt dung riêng | Energy needed to raise the temperature of one unit mass by one kelvin. | `cₚ`; `J/(kg·K)`. |
| thermal expansion | giãn nở nhiệt | Change in size caused by a temperature change. | Linear coefficient `α`; `1/K`. |
| pressure | áp suất | Normal force applied per unit area. | `p`; pascal (`Pa`), kilopascal (`kPa`), bar. |
| absolute pressure | áp suất tuyệt đối | Pressure measured relative to a perfect vacuum. | `p_abs`; always non-negative. |
| gauge pressure | áp suất dư; áp suất tương đối | Pressure measured relative to local atmospheric pressure. | `p_gauge = p_abs - p_atm`. |
| flow rate | lưu lượng | Amount of fluid passing a section per unit time. | Volume flow `m³/s`; mass flow `kg/s`. |
| viscosity | độ nhớt | Resistance of a fluid to shearing flow. | Dynamic viscosity `μ`; `Pa·s`. |
| kinematic viscosity | độ nhớt động học | Dynamic viscosity divided by density. | `ν`; `m²/s`, often `mm²/s` or `cSt`. |
| compressible flow | dòng chảy nén được | Flow in which density changes are important. | Important for intake air, exhaust gas, and turbochargers. |
| incompressible flow | dòng chảy không nén được | Approximation in which fluid density is treated as constant. | Often used for liquid fuel, coolant, and brake fluid. |
| laminar flow | dòng chảy tầng | Ordered flow with limited mixing between layers. | Usually associated with lower Reynolds number. |
| turbulent flow | dòng chảy rối | Irregular flow with strong mixing and velocity fluctuations. | Common in engines, ducts, and external aerodynamics. |
| Reynolds number | số Reynolds | Ratio comparing inertial and viscous effects in fluid flow. | `Re`; dimensionless. |

## Vehicle Architecture

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| vehicle architecture | kiến trúc xe | High-level arrangement of major structures, systems, and interfaces. | Includes platform, powertrain layout, electrical architecture, and packaging. |
| vehicle platform | nền tảng xe; khung gầm nền tảng | Shared engineering base used for one or more vehicle models. | May share underbody, hard points, modules, or manufacturing processes. |
| packaging | bố trí không gian; bố trí tổng thể | Work of fitting occupants, cargo, components, clearances, and service access into the vehicle. | A design activity, not product packaging. |
| hard point | điểm chuẩn hình học; điểm cố định thiết kế | A controlled reference location that strongly constrains component geometry. | Examples: suspension pickup or seat mounting point. |
| body-on-frame | thân xe đặt trên khung rời | Construction with a separate structural frame supporting the body. | Common in some trucks and off-road vehicles. |
| unibody | thân liền khung; thân xe tự chịu lực | Construction in which the body structure carries most vehicle loads. | Also called unitized body or monocoque in common automotive usage. |
| monocoque | kết cấu vỏ chịu lực | Structure in which the outer shell carries structural load. | Real cars often use semi-monocoque or unitized construction. |
| space frame | khung không gian | Three-dimensional frame made from connected structural members. | Body panels may carry little structural load. |
| frame | khung xe | Main load-carrying structural assembly. | Can refer to a ladder frame or another separate frame. |
| subframe | khung phụ | Structural module attached to the body or frame to support systems. | Often supports the engine, suspension, or rear axle. |
| body-in-white (BIW) | thân vỏ trắng; thân xe chưa sơn | Welded or joined body structure before paint, trim, and major systems are installed. | `BIW`. Exact production boundary can vary. |
| wheelbase | chiều dài cơ sở | Longitudinal distance between the front and rear axle or wheel centers. | `L`; millimetre (`mm`). |
| track width | chiều rộng vệt bánh xe | Lateral distance between left and right wheel centerlines on one axle. | Front and rear track may differ; `mm`. |
| overhang | phần nhô trước hoặc sau | Distance from an axle centerline to the nearest end of the vehicle. | Front overhang and rear overhang; `mm`. |
| ground clearance | khoảng sáng gầm xe | Vertical distance between the ground and a specified lowest vehicle point. | Definition and loading condition must be stated; `mm`. |
| ride height | chiều cao vận hành; độ cao thân xe | Height of specified body or suspension reference points above the ground. | Depends on vehicle load and suspension setting. |
| curb mass | khối lượng bản thân xe | Mass of a vehicle ready for normal operation under a stated definition, without payload. | Also `kerb mass`; definitions vary by regulation. Unit `kg`. |
| gross vehicle mass (GVM) | khối lượng toàn bộ của xe | Actual total vehicle mass at a given condition or a permitted maximum, depending on context. | Confirm whether the document means actual or rated mass; `kg`. |
| gross vehicle weight rating (GVWR) | khối lượng toàn bộ cho phép lớn nhất | Manufacturer's maximum permitted loaded vehicle weight rating. | `GVWR`; expressed as mass in common specifications. |
| payload | tải trọng hữu ích | Mass of occupants, cargo, and other carried load permitted or present. | `kg`; calculation definition can vary. |
| sprung mass | khối lượng được treo | Vehicle mass supported by the suspension springs. | Mainly body, occupants, cargo, and supported systems. |
| unsprung mass | khối lượng không được treo | Mass that moves mainly with the wheels rather than being supported by the springs. | Includes wheels and parts of brakes, hubs, and suspension. |
| center of gravity (CG) | trọng tâm | Point through which the resultant gravitational force is treated as acting. | `CG` or `CoG`; location changes with loading. |
| front-wheel drive (FWD) | dẫn động cầu trước | Layout in which the front wheels receive propulsion torque. | `FWD`. |
| rear-wheel drive (RWD) | dẫn động cầu sau | Layout in which the rear wheels receive propulsion torque. | `RWD`. |
| all-wheel drive (AWD) | dẫn động tất cả các bánh | System capable of delivering propulsion torque to front and rear axles. | `AWD`; operation and torque split vary. |
| four-wheel drive (4WD) | dẫn động bốn bánh | Four-wheel driveline term often used for selectable or off-road-focused systems. | `4WD` or `4x4`; boundary from AWD is not universal. |

## Aerodynamics And Performance

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| aerodynamic drag | lực cản khí động | Force opposing vehicle motion through air. | `F_D = ½ρv²C_DA`; newton (`N`). |
| drag coefficient | hệ số cản khí động | Dimensionless coefficient describing aerodynamic drag independent of size in a chosen reference system. | `C_D`; dimensionless. |
| frontal area | diện tích cản chính diện | Projected vehicle area seen from the front. | `A`; `m²`. |
| drag area | diện tích cản tương đương | Product of drag coefficient and frontal area. | `C_DA`; `m²`. Useful for comparing total drag tendency. |
| aerodynamic lift | lực nâng khí động | Aerodynamic force perpendicular to the airflow reference direction. | `F_L`; `N`. Positive sign convention must be stated. |
| downforce | lực ép khí động | Aerodynamic force pressing a vehicle toward the road. | Often treated as negative lift; `N`. |
| lift coefficient | hệ số lực nâng | Dimensionless coefficient describing aerodynamic lift. | `C_L`; dimensionless. Sign convention matters. |
| rolling resistance | lực cản lăn | Force resisting rolling, mainly from tire deformation and energy loss. | `F_rr`; `N`. |
| rolling-resistance coefficient | hệ số cản lăn | Ratio used in a simple model of rolling resistance to normal load. | `C_rr`; dimensionless. |
| gradeability | khả năng leo dốc | Ability of a vehicle to climb a specified slope under stated conditions. | Often percent grade or angle. |
| tractive effort | lực kéo tại bánh xe | Longitudinal force available at the tire-road interface to propel the vehicle. | `F_t`; `N`. |
| top speed | tốc độ tối đa | Highest steady vehicle speed under stated conditions. | `km/h` or `m/s`; limited by power, gearing, control, or tires. |
| zero-to-one-hundred time | thời gian tăng tốc 0–100 km/h | Time taken to accelerate from rest to `100 km/h`. | Second (`s`); test conditions matter. |
| fuel economy | mức tiết kiệm nhiên liệu | Distance travelled per amount of fuel. | Examples: `km/L`, `mpg`. Inverse of fuel consumption. |
| fuel consumption | mức tiêu thụ nhiên liệu | Fuel volume or mass used per distance or time. | Common road unit `L/100 km`. |
| energy consumption | mức tiêu thụ năng lượng | Energy used per distance, often for electric vehicles. | `Wh/km` or `kWh/100 km`. |
| driving range | quãng đường di chuyển | Distance achievable before refuelling or recharging under stated conditions. | `km`; test cycle and environment strongly affect it. |

## Noise And Vibration

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| noise, vibration, and harshness (NVH) | tiếng ồn, rung động và độ khắc nghiệt | Engineering field concerned with audible noise, felt vibration, and subjective refinement. | `NVH`. Harshness is partly subjective. |
| sound pressure level (SPL) | mức áp suất âm | Logarithmic measure of sound pressure relative to a reference. | `L_p`; decibel (`dB`). Weighting such as `dB(A)` must be stated. |
| frequency | tần số | Number of repeating cycles per second. | `f`; hertz (`Hz`). |
| amplitude | biên độ | Magnitude of an oscillating signal or motion. | Unit depends on quantity: `m`, `m/s²`, `Pa`, and others. |
| vibration | rung động | Oscillating mechanical motion about an equilibrium position. | Measured as displacement, velocity, or acceleration. |
| harshness | độ khắc nghiệt; cảm giác xóc gắt | Subjective perception of short, unpleasant vibration or noise events. | No single universal unit. |
| booming noise | tiếng ù tần số thấp | Low-frequency cabin noise often linked to body or acoustic resonance. | Frequency range depends on vehicle and source. |
| road noise | tiếng ồn từ mặt đường | Noise generated by tire-road interaction and transmitted to the cabin. | Depends on tires, surface, speed, and isolation. |
| wind noise | tiếng ồn khí động | Noise produced by airflow around seals, mirrors, pillars, and body surfaces. | Usually increases strongly with speed. |

[Back to terminology index](README.md)
