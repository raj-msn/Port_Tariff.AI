Based on the document provided, here are the extracted rules and formulas for the specified dues.

### **Light Dues**
*(Source: Page 5)*

#### **General Rules and Guidelines:**
*   Light Dues are calculated based on the vessel's gross tonnage as per the Tonnage Convention 1969. If a tonnage certificate is not available, the highest tonnage from the Lloyds Register of Shipping is used.
*   For "All other vessels" (not registered locally for this purpose), dues are raised at the first South African port of call and are valid until the vessel departs from the last South African port of call, subject to two conditions:
    1.  The vessel does not travel beyond the South African coastline.
    2.  The time spent in South African waters does not exceed 60 days.
*   If a vessel stays longer than 60 days, it is considered "coastal" and becomes liable for Light Dues on a per-calendar-month basis.
*   Coasters under a "Bonafide Coasters" status have a special monthly agreement.

#### **Exemptions:**
A 100% reduction is granted for:
*   South African Police Services (SAPS) and South African National Defence Force (SANDF) vessels.
*   SAMSA vessels.
*   SA Medical & Research vessels.
*   Non-self-propelled small and pleasure vessels not used for gain.
*   Vessels at anchorage outside the port, unless moored at a single buoy mooring or similar facility.
*   Foreign naval/war vessels are exempt from the SAMSA levy.

#### **Data Tables:**

| Category                                                                                                  | Rate                                                                    |
| :-------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------- |
| Self-propelled vessels, licensed by the Dept. of Environmental Affairs & Tourism, at their registered port | R 24.64 per metre (or part thereof) of length overall, per financial year |
| All other vessels                                                                                         | R 117.08 per 100 tons (or part thereof) of gross tonnage                  |

#### **Formulas:**
1.  **For self-propelled vessels at their registered port:**
    `Light Dues = 24.64 * ceil(Vessel_Length_in_Metres)`

2.  **For all other vessels:**
    `Light Dues = 117.08 * ceil(Gross_Tonnage / 100)`

---

### **VTS (Vessel Traffic Services) Dues**
*(Source: Page 6)*

#### **General Rules and Guidelines:**
*   VTS charges are for safe navigation, pollution, and conservancy, based on the vessel's gross tonnage.
*   The charge is payable by vessels calling at any port under the Authority's control and vessels performing port-related services within port limits.
*   A minimum fee applies to all calculations.

#### **Exemptions:**
*   SAPS and SANDF vessels.
*   SAMSA vessels.
*   SA Medical & Research vessels.
*   Vessels returning from anchorage by order of the Harbour Master.
*   Small vessels and pleasure vessels (as defined in Section 4, Clause 4.2).

#### **Data Tables:**

| Location                                            | Rate per GT per Port Call | Minimum Fee |
| :-------------------------------------------------- | :------------------------ | :---------- |
| All ports **excluding** Durban and Saldanha Bay       | R 0.54                    | R 235.52    |
| Ports of Durban and Saldanha Bay                    | R 0.65                    | R 235.52    |

#### **Formulas:**
1.  **For ports excluding Durban and Saldanha Bay:**
    `VTS Dues = max(235.52, 0.54 * Gross_Tonnage)`

2.  **For the ports of Durban and Saldanha Bay:**
    `VTS Dues = max(235.52, 0.65 * Gross_Tonnage)`

---

### **Pilotage Dues**
*(Source: Page 7)*

#### **General Rules and Guidelines:**
*   Pilotage is compulsory at the ports of Richards Bay, Durban, East London, Ngqura, Port Elizabeth, Mossel Bay, Cape Town, and Saldanha.
*   The fee is charged per service (e.g., entering or leaving the port) and consists of a Basic Fee plus a tonnage-based charge.
*   A **50% surcharge** is applied at all ports in the following instances:
    *   The service commences or terminates outside ordinary working hours.
    *   The vessel is not ready to move 30 minutes after the notified time or 30 minutes after the pilot has boarded (whichever is later).
    *   The service request is cancelled within 30 minutes of the notified time and the pilot has not boarded.
*   At the **Port of Durban**, a 50% surcharge applies if the service is cancelled within 60 minutes prior to the notified time and the pilot has not boarded.

#### **Exemptions:**
*   SAPS and SANDF vessels are exempt, unless pilotage services are specifically requested.

#### **Data Tables:**

| Port                      | Basic Fee per Service | Rate per 100 tons (or part thereof) |
| :------------------------ | :-------------------- | :---------------------------------- |
| Richards Bay              | R 30,960.46           | R 10.93                             |
| Durban                    | R 18,608.61           | R 9.72                              |
| Port Elizabeth / Ngqura   | R 8,970.00            | R 14.33                             |
| Cape Town                 | R 6,342.39            | R 10.20                             |
| Saldanha                  | R 9,673.57            | R 13.66                             |
| Other                     | R 6,547.45            | R 10.49                             |

#### **Formulas:**
1.  **Calculate Base Pilotage Dues:**
    `Base Dues = Basic_Fee + (Rate_per_100_tons * ceil(Gross_Tonnage / 100))`

2.  **Calculate Total Dues with Surcharge (if applicable):**
    `Total Dues = Base Dues * (1 + Surcharge_Percentage)`

---

### **Towage Dues (Tugs/Vessel Assistance)**
*(Source: Page 8)*

#### **General Rules and Guidelines:**
*   Fees are for tugs assisting or attending vessels within the port, charged per service and based on the vessel's gross tonnage.
*   The fee structure is tiered, with a base fee for a given tonnage bracket plus an incremental charge for tonnage exceeding the bracket's lower limit.
*   A **25% surcharge** applies for services commencing or terminating outside ordinary working hours, on weekdays, Saturdays, Sundays, or public holidays.
*   A **50% surcharge** is payable per tug if an additional tug is requested by the master or deemed necessary for safety.
*   A **50% surcharge** is payable when servicing a vessel without its own power. This increases to a **100% surcharge** if an additional tug is also provided.
*   If a vessel arrives or departs 30 minutes or more after the notified time, a delay fee is charged per tug per half hour (or part thereof):
    *   **All ports (except Saldanha):** R 8,050.76
    *   **Port of Saldanha:** R 10,152.19

#### **Data Tables:**
*The table below outlines the tiered, incremental charges per port. To calculate the fee, find the vessel's tonnage bracket, take the base fee (top row in cell), and add the incremental charge (bottom row in cell) for every 100 tons over the bracket's lower bound.*

| Tonnage Bracket     | Richards Bay | Durban     | East London | Port Elizabeth / Ngqura | Mossel Bay | Cape Town  | Saldanha   |
| :------------------ | :----------- | :--------- | :---------- | :---------------------- | :--------- | :--------- | :--------- |
| **Up to 2,000**     | R 7,001.67   | R 8,140.00 | R 5,622.16  | R 7,206.98              | R 6,316.53 | R 5,411.47 | R 9,038.42 |
| **2,001 to 10,000** | R 13,020.67  | R 12,633.99| R 8,152.14  | R 11,168.45             | R 8,152.14 | R 7,898.57 | R 15,378.78|
| *Plus per 100 tons* | R 275.32     | R 268.99   | R 200.97    | R 237.53                | R 173.37   | R 194.63   | R 327.43   |
| **10,001 to 50,000**| R 39,999.88  | R 38,494.51| R 27,956.91 | R 32,257.98             | R 25,806.37| R 27,741.85| R 47,311.70|
| *Plus per 100 tons* | R 101.08     | R 84.95    | R 66.67     | R 73.10                 | R 60.21    | R 64.52    | R 103.23   |
| **50,001 to 100,000**| R 79,999.76  | R 73,118.07| R 55,913.82 | R 64,515.95             | n/a        | R 53,978.33| R 90,322.33|
| *Plus per 100 tons* | R 30.11      | R 32.24    | R 25.80     | R 21.50                 | n/a        | R 47.32    | R 27.97    |
| **Above 100,000**   | R 103,999.70 | R 93,548.13| n/a         | R 82,542.46             | n/a        | R 79,569.67| R 111,827.63|
| *Plus per 100 tons* | R 21.50      | R 23.65    | n/a         | R 21.50                 | n/a        | R 38.71    | R 47.32    |

#### **Formulas:**
1.  **Calculate Base Towage Dues:**
    *   Identify the vessel's tonnage bracket and the corresponding port.
    *   `Excess Tonnage = Gross_Tonnage - Bracket_Lower_Bound`
    *   `Incremental Units = ceil(Excess_Tonnage / 100)`
    *   `Base Dues = Bracket_Base_Fee + (Incremental_Units * Incremental_Rate_per_100_tons)`

2.  **Example (35,000 GT vessel in Durban):**
    *   Bracket: 10,001 to 50,000
    *   Bracket Base Fee: R 38,494.51
    *   Incremental Rate: R 84.95
    *   Excess Tonnage: 35,000 - 10,000 = 25,000
    *   Incremental Units: ceil(25,000 / 100) = 250
    *   `Base Dues = 38494.51 + (250 * 84.95) = 38494.51 + 21237.50 = R 59,732.01`

---

### **Port Dues**
*(Source: Page 11)*

#### **General Rules and Guidelines:**
*   Port Dues are payable by vessels entering the port, from passing the entrance inwards until passing outwards.
*   **NOTE:** The provided document specifies rates for vessels "at offshore moorings or similar facilities." A general rate for vessels berthing alongside a commercial quay is not explicitly stated in this section. The rules below apply to the rates that are provided.
*   A **35% reduction** is allowed for:
    *   Vessels not working cargo for the first 30 days.
    *   Bona fide coasters.
    *   Passenger vessels.
*   A **60% reduction** is allowed for vessels calling *only* for bunkers, stores, or water, provided the stay does not exceed 48 hours. This reduction cannot be combined with the 35% reduction.
*   A **10% reduction** is allowed for certified double-hulled tankers, tankers with segregated ballast tanks, or those with a "Green Award."
*   A **15% reduction** is allowed for vessels in port for less than 12 hours.
*   A **20% surcharge** on the incremental fee is applied to vessels in port longer than 30 days that are not working cargo or undergoing repairs.

#### **Exemptions:**
*   SAPS and SANDF vessels.
*   SAMSA vessels.
*   SA Medical & Research vessels.
*   The time a vessel occupies a drydock, floating dock, syncrolift, or slipway.
*   Vessels returning from anchorage by order of the port.

#### **Data Tables (For vessels at offshore moorings or similar facilities):**

| Fee Type                                | Rate                                          |
| :-------------------------------------- | :-------------------------------------------- |
| Basic Fee                               | R 192.73 per 100 tons (or part thereof)       |
| Time-based Fee (added to Basic Fee)     | R 57.79 per 100 tons (or part thereof) per 24-hour period (pro-rata) |

#### **Formulas (For vessels at offshore moorings):**
1.  **Calculate Base Port Dues:**
    `Initial Fee = 192.73 * ceil(Gross_Tonnage / 100)`
    `Daily Fee = 57.79 * ceil(Gross_Tonnage / 100) * (Duration_in_hours / 24)`
    `Base Dues = Initial Fee + Daily Fee`

2.  **Apply Reductions and Surcharges:**
    `Final Dues = Base Dues * (1 - Reduction_1) * (1 - Reduction_2) * ... * (1 + Surcharge_Percentage)`

---

### **Running of Vessel Lines Dues**
*(Source: Page 10)*

#### **General Rules and Guidelines:**
*   Fees are for using a launch/mooring boat to run a vessel's lines from the ship to the bollard during entering, leaving, or shifting.
*   Fees are charged per service and vary by port.
*   A higher minimum charge applies for services that terminate or commence outside ordinary working hours.
*   If a vessel's arrival or departure is delayed by 30 minutes or more, a separate set of hourly rates applies, calculated from the notified time until the service is completed.

#### **Data Tables:**
**Table 1: Standard Service (On-time)**
| Port                    | Fee per Service | Minimum Fee (Outside Ordinary Hours) |
| :---------------------- | :-------------- | :----------------------------------- |
| Port Elizabeth / Ngqura | R 2,266.73      | R 4,533.42                           |
| Cape Town               | R 2,370.84      | R 3,309.05                           |
| Saldanha                | R 2,085.59      | R 4,171.18                           |
| Other Ports             | R 1,654.56      | R 3,309.05                           |

**Table 2: Delayed Service (Per hour or part thereof)**
| Port                    | Hourly Rate | Minimum Fee (Outside Ordinary Hours) |
| :---------------------- | :---------- | :----------------------------------- |
| Port Elizabeth / Ngqura | R 2,266.73  | R 4,533.42                           |
| Cape Town               | R 2,370.84  | R 4,741.69                           |
| Saldanha                | R 2,085.59  | R 4,171.18                           |
| Other Ports             | R 1,654.56  | R 3,309.05                           |

#### **Formulas:**
1.  **On-time Service (Normal Hours):**
    `Dues = Fee per Service` (from Table 1)

2.  **On-time Service (Outside Hours):**
    `Dues = Minimum Fee` (from Table 1)

3.  **Delayed Service (Normal Hours):**
    `Dues = Hourly Rate * ceil(Delay_in_Hours)` (from Table 2)

4.  **Delayed Service (Outside Hours):**
    `Calculated Hourly Dues = Hourly Rate * ceil(Delay_in_Hours)` (from Table 2)
    `Dues = max(Calculated Hourly Dues, Minimum Fee)` (from Table 2)