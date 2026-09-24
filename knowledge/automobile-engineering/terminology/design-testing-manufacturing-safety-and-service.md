# Design, Testing, Manufacturing, Safety, And Service Terms

These terms describe the engineering lifecycle from requirements and design to production, validation, maintenance, and repair.

## Table Of Contents

- [Requirements And Design](#requirements-and-design)
- [Analysis And Testing](#analysis-and-testing)
- [Materials And Manufacturing](#materials-and-manufacturing)
- [Safety And Regulation](#safety-and-regulation)
- [Reliability Quality And Service](#reliability-quality-and-service)

## Requirements And Design

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| requirement | yêu cầu | Clear, testable statement of a needed function, performance, interface, or constraint. | Good requirements define conditions and acceptance criteria. |
| specification | đặc tả; thông số kỹ thuật | Controlled description of technical requirements and characteristics. | Can describe a system, component, material, process, or test. |
| constraint | ràng buộc | Limit that restricts possible design choices. | Examples: cost, mass, space, regulation, temperature. |
| target | mục tiêu kỹ thuật | Desired performance value used to guide development. | Target is not automatically a verified result. |
| acceptance criterion | tiêu chí chấp nhận | Measurable condition deciding whether an item or test passes. | Includes limit, condition, method, and sometimes confidence. |
| use case | trường hợp sử dụng | Description of how a user or external actor interacts with a system to reach a goal. | Used to derive functions and requirements. |
| operating condition | điều kiện vận hành | Defined environment and state in which performance is evaluated. | Load, speed, voltage, temperature, road, and altitude may matter. |
| boundary condition | điều kiện biên | Constraint or input applied at the boundary of an analysis or test model. | Strongly affects simulation results. |
| interface | giao diện; điểm giao tiếp | Defined boundary where systems exchange force, energy, material, data, or geometry. | Mechanical, electrical, thermal, fluid, or software. |
| architecture | kiến trúc hệ thống | High-level structure of components, functions, connections, and responsibilities. | Physical, electrical, software, or functional architecture. |
| subsystem | hệ thống con | Part of a larger system with a defined function and interfaces. | Example: braking subsystem. |
| component | bộ phận; linh kiện | Individual item within an assembly or system. | Hardware or software component. |
| assembly | cụm lắp ráp | Group of parts joined to perform a function or form a production unit. | Can contain subassemblies. |
| bill of materials (BOM) | danh mục vật tư; danh sách cấu kiện | Structured list of parts, quantities, and relationships needed to build a product. | `BOM`; engineering and manufacturing BOMs can differ. |
| trade-off | sự đánh đổi kỹ thuật | Decision balancing competing objectives when improving one can worsen another. | Examples: mass versus cost, comfort versus handling. |
| design margin | biên dự phòng thiết kế | Difference or ratio between expected capability and required demand. | Definition must state direction and statistical basis. |
| factor of safety | hệ số an toàn | Ratio comparing failure capacity with allowable working demand under a chosen definition. | Dimensionless; exact formula varies by discipline. |
| tolerance stack-up | chuỗi dung sai | Combined effect of dimensional variations across connected parts. | Worst-case or statistical method. |
| design review | đánh giá thiết kế | Structured examination of design evidence, risks, interfaces, and readiness. | Review does not replace verification. |
| change control | kiểm soát thay đổi | Process for evaluating, approving, recording, and releasing changes. | Protects configuration consistency and traceability. |
| configuration | cấu hình | Defined combination of product hardware, software, calibration, and options. | Must be controlled during testing and production. |
| traceability | khả năng truy xuất | Ability to link needs, requirements, design, implementation, tests, results, and changes. | Supports safety, quality, and impact analysis. |

## Analysis And Testing

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| computer-aided design (CAD) | thiết kế có sự hỗ trợ của máy tính | Digital creation and control of geometry, drawings, and product definition. | `CAD`; 2D and 3D. |
| computer-aided engineering (CAE) | kỹ thuật có sự hỗ trợ của máy tính | Use of simulation and analysis tools to evaluate designs. | `CAE`; includes FEA, CFD, multibody, and system simulation. |
| finite-element analysis (FEA) | phân tích phần tử hữu hạn | Numerical method dividing a model into elements to estimate stress, deformation, heat, vibration, and other fields. | `FEA`; result quality depends on model and validation. |
| computational fluid dynamics (CFD) | động lực học chất lưu tính toán | Numerical analysis of fluid flow, heat transfer, and related phenomena. | `CFD`; mesh and turbulence model affect results. |
| multibody dynamics (MBD) | động lực học hệ nhiều vật | Simulation of interconnected rigid or flexible bodies, joints, forces, and motion. | `MBD`; common for suspension and full-vehicle models. |
| one-dimensional simulation (1D simulation) | mô phỏng một chiều; mô phỏng hệ thống | System-level simulation using lumped components and flow paths. | `1D`; common for thermal, fluid, powertrain, and energy analysis. |
| model | mô hình | Simplified representation of a real system used for understanding, prediction, or control. | Every model has assumptions and limits. |
| simulation | mô phỏng | Execution of a model to study behaviour under defined inputs and conditions. | Simulation is evidence, not automatic proof. |
| correlation | tương quan; đối chiếu mô hình–thử nghiệm | Degree of agreement or statistical relationship between datasets. | Correlation does not by itself prove causation. |
| verification | xác minh | Checking that a design, model, or implementation meets specified requirements or was built correctly. | Often summarized as “built right.” |
| validation | xác nhận giá trị sử dụng | Checking that the product meets intended user needs in its real or representative context. | Often summarized as “built the right thing.” |
| test plan | kế hoạch thử nghiệm | Controlled description of test objectives, items, methods, conditions, equipment, and acceptance criteria. | Includes responsibilities and data handling where needed. |
| test procedure | quy trình thử nghiệm | Step-by-step instructions for executing a test consistently. | Must identify setup and safety precautions. |
| test case | ca kiểm thử | Defined input, condition, execution, and expected result for one test objective. | Used in software and system testing. |
| test fixture | đồ gá thử nghiệm | Equipment holding, loading, connecting, or positioning a test item. | Fixture influence must be understood. |
| instrumentation | hệ thống đo lường thử nghiệm | Sensors, signal conditioning, acquisition, and tools used to collect test data. | Includes calibration and sampling design. |
| data acquisition system (DAQ) | hệ thống thu thập dữ liệu | Hardware and software recording synchronized measurement signals. | `DAQ`; sample rate, range, resolution, and filtering matter. |
| repeatability | độ lặp lại | Agreement of results under the same method, equipment, operator, and short-term conditions. | A precision concept. |
| reproducibility | độ tái lập | Agreement of results when relevant conditions such as operator, equipment, or laboratory change. | Broader than repeatability. |
| test track | đường thử | Controlled road facility for vehicle performance, durability, safety, and handling tests. | Surface and manoeuvre are specified. |
| proving ground | bãi thử xe | Large controlled facility containing multiple specialized vehicle test roads and areas. | Used for development and validation. |
| dynamometer | băng thử động lực | Device applying and measuring force, torque, speed, and power. | Engine, motor, hub, or chassis dynamometer. |
| chassis dynamometer | băng thử công suất ô tô | Roller or hub system loading a complete vehicle through its driven wheels. | Measures wheel-level performance under controlled conditions. |
| wind tunnel | hầm gió | Facility producing controlled airflow around a vehicle or model. | Used for aerodynamics, cooling, wind noise, and contamination. |
| climatic chamber | buồng thử khí hậu | Controlled enclosure reproducing temperature, humidity, solar, or icing conditions. | Can test components or full vehicles. |
| durability test | thử nghiệm độ bền lâu | Test applying repeated or severe usage to evaluate life and degradation. | Acceleration factor and damage equivalence must be justified. |
| fatigue | mỏi vật liệu | Progressive damage under repeated or fluctuating load. | Can fail below static ultimate strength. |
| load case | trường hợp tải | Defined combination of forces, moments, constraints, and environment for analysis or test. | Normal, peak, misuse, crash, or fatigue cases. |

## Materials And Manufacturing

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| material property | tính chất vật liệu | Measurable characteristic describing material behaviour. | Depends on composition, process, temperature, and test method. |
| elastic deformation | biến dạng đàn hồi | Reversible deformation removed when load is released. | Below elastic limit under the relevant condition. |
| plastic deformation | biến dạng dẻo | Permanent deformation remaining after load removal. | Begins after yield under a simple tensile interpretation. |
| Young's modulus | mô-đun đàn hồi Young | Ratio of normal stress to elastic strain in a linear region. | `E`; pascal (`Pa`), commonly gigapascal (`GPa`). |
| yield strength | giới hạn chảy | Stress at which specified permanent deformation begins under a defined test. | `MPa`; proof strength may be used when no clear yield point exists. |
| ultimate tensile strength (UTS) | độ bền kéo lớn nhất | Maximum engineering tensile stress reached in a tensile test. | `UTS`; megapascal (`MPa`). |
| ductility | độ dẻo | Ability to undergo plastic deformation before fracture. | Measured by elongation or area reduction under a defined test. |
| toughness | độ dai | Ability to absorb energy before fracture. | Not the same as hardness or strength. |
| hardness | độ cứng bề mặt | Resistance to localized indentation or scratching under a defined test. | Scales include Rockwell, Vickers, and Brinell. |
| corrosion | ăn mòn | Material degradation through chemical or electrochemical interaction with environment. | Galvanic corrosion needs dissimilar materials and electrolyte. |
| steel | thép | Iron-based alloy with controlled carbon and other elements. | Grades vary widely in strength, formability, and coating. |
| cast iron | gang | Iron-carbon alloy with relatively high carbon, commonly produced by casting. | Grey, ductile, and other forms differ. |
| aluminium alloy | hợp kim nhôm | Aluminium-based material alloyed for strength, forming, casting, or corrosion performance. | Lower density than steel; stiffness per thickness differs. |
| composite material | vật liệu composite; vật liệu tổng hợp | Material combining distinct constituents to achieve useful properties. | Fibre-reinforced polymer is one class. |
| polymer | polyme; vật liệu nhựa | Material made from long-chain molecules, used in plastics, elastomers, adhesives, and coatings. | Behaviour depends strongly on temperature and time. |
| casting | đúc | Manufacturing by pouring or injecting liquid material into a mould and solidifying it. | Sand, die, investment, and other processes. |
| forging | rèn; dập rèn | Shaping material using compressive force, often improving grain flow and strength. | Hot, warm, or cold forging. |
| stamping | dập tấm | Cutting and forming sheet material with presses and dies. | Common for body panels and structural parts. |
| extrusion | ép đùn | Forcing material through a shaped die to make a continuous profile. | Common for aluminium structural members. |
| machining | gia công cắt gọt | Removing material with controlled tools to create geometry and surface finish. | Turning, milling, drilling, grinding. |
| welding | hàn | Joining materials using heat, pressure, or both, with or without filler. | Resistance spot welding is common in body production. |
| brazing | hàn vảy cứng | Joining with filler metal melting above 450 °C while base materials do not melt. | Different from welding and soldering. |
| adhesive bonding | liên kết bằng keo | Joining surfaces using a cured adhesive layer. | Can distribute load and join dissimilar materials. |
| injection moulding | ép phun | Manufacturing polymer parts by injecting molten material into a mould. | High tooling cost, efficient high-volume production. |
| additive manufacturing | chế tạo bồi đắp; in 3D | Building a part layer by layer from digital geometry. | Useful for prototypes, tooling, and selected production parts. |
| heat treatment | nhiệt luyện | Controlled heating and cooling to change material microstructure and properties. | Process depends on alloy and objective. |
| surface treatment | xử lý bề mặt | Process changing surface properties for corrosion, wear, appearance, or bonding. | Coating, plating, anodizing, shot peening, and others. |
| assembly line | dây chuyền lắp ráp | Production arrangement where product moves through ordered workstations. | Manual and automated operations can coexist. |
| takt time | nhịp sản xuất | Available production time divided by customer demand. | Time per required unit; not the same as cycle time. |
| cycle time | thời gian chu kỳ | Time needed to complete an operation or produce one unit at a process. | Compare with takt time for capacity planning. |
| poka-yoke | cơ cấu chống sai lỗi | Design or method preventing an error or making it immediately detectable. | Japanese manufacturing term. |
| torque specification | thông số mô-men siết | Controlled fastener installation requirement. | `N·m`; may also require angle, sequence, and lubrication state. |
| bolt preload | lực siết trước của bu-lông | Tensile force created in a fastener during tightening. | Newton (`N`); joint clamp force is the design purpose of torque control. |

## Safety And Regulation

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| active safety | an toàn chủ động | Functions intended to help avoid or control an incident before impact. | Examples: ABS, ESC, AEB. Boundary varies. |
| passive safety | an toàn bị động | Features intended to reduce injury during and after a crash. | Structure, restraints, airbags, and post-crash functions. |
| crashworthiness | khả năng bảo vệ khi va chạm | Ability of a vehicle structure and restraint system to protect occupants in crashes. | Evaluated for defined crash modes and occupants. |
| crumple zone | vùng biến dạng hấp thụ xung lực | Structure designed to deform and absorb crash energy in a controlled manner. | Must work with survival space and restraints. |
| occupant compartment | khoang hành khách | Structural space intended to remain sufficiently survivable for occupants. | Intrusion is a key measure. |
| restraint system | hệ thống bảo vệ giữ người | System controlling occupant motion in a crash. | Seat belt, pretensioner, load limiter, airbag, and seat. |
| seat belt | dây đai an toàn | Webbing restraint distributing forces and limiting occupant motion. | Three-point belt is common. |
| pretensioner | bộ căng đai khẩn cấp | Device removing belt slack at the start of a crash event. | Pyrotechnic or reversible electric type. |
| load limiter | bộ giới hạn lực dây đai | Feature controlling belt force by allowing managed webbing payout. | Works with airbag and vehicle structure. |
| airbag | túi khí | Inflatable restraint deploying during selected crash conditions. | Supplemental to seat belt, not a replacement. |
| supplemental restraint system (SRS) | hệ thống bảo vệ bổ sung | Electronic and pyrotechnic system controlling airbags and related restraints. | `SRS`. |
| side-impact beam | thanh gia cường chống va chạm bên | Door or body reinforcement helping manage lateral crash load. | One element of side-impact protection. |
| pedestrian protection | bảo vệ người đi bộ | Vehicle design and functions intended to reduce pedestrian collision risk or injury. | Includes sensing, braking, geometry, and deformable structures. |
| hazard | mối nguy | Potential source of harm. | Not the same as risk. |
| risk | rủi ro | Combination of probability and severity of harm under a defined method. | Assessment method must be stated. |
| functional safety | an toàn chức năng | Absence of unreasonable risk due to hazards caused by malfunctioning electrical/electronic behaviour. | Road vehicles commonly reference ISO 26262. |
| Automotive Safety Integrity Level (ASIL) | mức toàn vẹn an toàn ô tô | Risk-based classification used to define ISO 26262 safety rigor. | `ASIL A` through `ASIL D`; `D` is highest rigor. `QM` is outside ASIL. |
| safety goal | mục tiêu an toàn | Top-level safety requirement derived from a hazardous-event analysis. | Part of a functional-safety concept. |
| safe state | trạng thái an toàn | Operating state without unreasonable risk for a defined fault and situation. | Can differ by function and driving condition. |
| homologation | chứng nhận kiểu loại | Process of demonstrating that a vehicle or component complies with market regulations. | Usage overlaps with type approval. |
| type approval | phê duyệt kiểu loại | Regulatory approval of a representative product type before market entry. | Requirements vary by jurisdiction. |
| regulatory compliance | tuân thủ quy định | Evidence that applicable legal and technical requirements are satisfied. | Market, vehicle category, and production date matter. |
| New Car Assessment Program (NCAP) | chương trình đánh giá xe mới | Consumer-information crash and active-safety rating program. | `NCAP`; protocols differ by region and change over time. |
| recall | triệu hồi | Corrective action requesting affected products be inspected, repaired, or modified for a safety or compliance issue. | Legal process varies by country. |

## Reliability Quality And Service

| English term | Common Vietnamese | Engineering meaning | Symbol, unit, or note |
| --- | --- | --- | --- |
| quality | chất lượng | Degree to which inherent characteristics fulfil requirements. | Includes conformance and fitness for intended use. |
| reliability | độ tin cậy | Probability of performing required function without failure for stated time and conditions. | Must state mission, conditions, and success criteria. |
| durability | độ bền lâu | Ability to withstand use, environment, and degradation over expected life. | Related to reliability but not identical. |
| robustness | tính vững; khả năng chống biến thiên | Ability to maintain acceptable performance despite variation and disturbance. | Variation can come from production, ageing, users, or environment. |
| failure | hỏng; sự cố mất chức năng | Loss of ability to perform a required function. | Event, not necessarily the physical cause. |
| failure mode | dạng hỏng | Specific way an item fails to meet intended function. | Examples: open circuit, leak, fracture, stuck valve. |
| failure mechanism | cơ chế hỏng | Physical, chemical, electrical, or software process producing a failure. | Examples: fatigue, corrosion, wear, overheating. |
| failure effect | hậu quả của dạng hỏng | Consequence of a failure mode at local, subsystem, vehicle, or user level. | Used in FMEA. |
| failure mode and effects analysis (FMEA) | phân tích dạng hỏng và hậu quả | Structured method identifying potential failures, causes, controls, and effects. | `FMEA`; design `DFMEA` and process `PFMEA`. |
| root cause | nguyên nhân gốc | Underlying controllable cause that, when corrected, prevents recurrence within the defined system. | Do not confuse symptom with cause. |
| symptom | triệu chứng | Observable evidence of abnormal operation. | One symptom can have many causes. |
| fault | lỗi; tình trạng lỗi | Abnormal condition that may lead to failure or degraded behaviour. | Hardware, software, communication, or calibration fault. |
| diagnosis | chẩn đoán | Evidence-based process of identifying the cause and location of a fault. | Includes tests, data, hypotheses, and confirmation. |
| troubleshooting | xử lý tìm lỗi | Practical step-by-step process used to locate and correct a problem. | Good troubleshooting starts with symptom verification. |
| preventive maintenance | bảo dưỡng phòng ngừa | Planned work intended to reduce failure probability or degradation. | Time-, distance-, or condition-based. |
| corrective maintenance | bảo dưỡng sửa chữa | Work restoring function after a fault or failure is found. | Includes repair and replacement. |
| predictive maintenance | bảo dưỡng dự đoán | Maintenance timing based on measured condition and degradation prediction. | Requires useful monitoring and decision thresholds. |
| service interval | chu kỳ bảo dưỡng | Specified time, distance, or operating amount between service actions. | Follow vehicle-specific schedule and operating conditions. |
| service manual | tài liệu hướng dẫn sửa chữa | Controlled technical information for diagnosis, disassembly, repair, adjustment, and safety. | Vehicle and configuration-specific. |
| workshop manual | sổ tay sửa chữa | Another common name for detailed service information used by technicians. | Manufacturer terminology varies. |
| technical service bulletin (TSB) | bản tin dịch vụ kỹ thuật | Manufacturer communication giving diagnosis or repair guidance for known conditions. | `TSB`; not automatically a safety recall. |
| original equipment manufacturer (OEM) | nhà sản xuất thiết bị gốc | Company responsible for original vehicle or component product in the stated supply context. | `OEM`; meaning can shift across supply tiers. |
| aftermarket | thị trường phụ tùng sau bán hàng | Parts, accessories, and services supplied after original vehicle sale, often outside original production supply. | Includes OEM-branded and independent products depending on context. |
| vehicle identification number (VIN) | số nhận dạng xe; số khung VIN | Standardized vehicle identifier encoding manufacturer and vehicle information. | `VIN`; commonly 17 characters in many markets, but historical and regional exceptions exist. |
| part number | mã phụ tùng | Identifier assigned to a specific controlled part definition or service item. | Revision and supersession must be checked. |
| serial number | số sê-ri | Identifier for one individual manufactured item. | Different from a part number shared by a design. |
| wear | mài mòn | Progressive material loss or surface change caused by contact and relative motion. | Adhesive, abrasive, fatigue, and other wear modes. |
| leakage | sự rò rỉ | Unintended flow of fluid, gas, current, or information across a boundary. | Rate and acceptable limit must be defined. |
| mean time between failures (MTBF) | thời gian trung bình giữa các lần hỏng | Statistical average operating time between repairable-system failures under stated assumptions. | `MTBF`; not a guaranteed individual lifetime. |
| warranty | bảo hành | Supplier commitment to remedy defined defects under stated time, use, and coverage conditions. | Commercial/legal term, not a direct engineering life target. |

[Back to terminology index](README.md)
