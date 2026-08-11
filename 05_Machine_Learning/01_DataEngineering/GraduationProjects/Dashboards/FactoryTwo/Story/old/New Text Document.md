

**we have more than one factory every factory have their own products and their custom number of production lines, so now we design excel sheets for factory-2 but in database we will store for all factories whereas all of them have alot of things similar but they are different slightly let is go deep now for factory-2**



**in factory 2,** 



1. **we have 1 furnance that have 5 distributer every distributer feeds one press machine and then we have 5 pressing machine, every machine have their custom number of sections and every section perhabs works one cavity or 2 cavities or three according to if we in production or make trial and also according to the product perhabs we operate 2 cavities for a product and 3 cavities for another product on the same machine. also perhabs we out a cavity in caustom section on a machine cause have high reject rate so we out it until root cause detection and solve it**
2. **we have 2 main shifts called AM and PM, and workers splitted to 3 groups A, B, C perhabs this day or week group A works in Am and Group B work in Pm and Group C in vacation so this matter depend on the production workforce planning**
3. **with respect to product and customer and order, we have product name assigned to unidue product code. also we have 2 main cateogries of container products whtheer it will be jars or botlles. we have multiple customers perhabs the customer can be existed in our country or it can be in foreign country, evey single customer can have own multiple products or it can have only one product. with respect to order we have order number and for any order we producr total molten units that can be classified later**
4. **in any line there are 3 cases first one normal production, second one we make trial, third one reworking given that reworking have 3 status {Hold, Resorted, Move to callet}**
5. **in normal production, for every machine from 5 machines, we have designed values like cycles (cur/min) it is custom to every machine, also design number of cavity for every machine, and number of sections so we design speed of machine by calcauting in  one min how much cuts should be designed for production so if every section have 10 cycle per min and have 3 cavities in 10 section so should 3\*10\*10\*60 will give us no of cuts in hour for machine and so on we compare actual produced with the designed one. given actual produced have percent of rejection and other perecent as accepted and perhabs some percent to be reworked and we will handle reworked later**
6. **in trial, we measure the losses time to make that trail on custome machine and result of that trail where trail can be for new product or after make modification on the machine or after redesign product also as result of trail we measure losses in units where as weagreed before furncace have 5 distributer and distributer will be worked without stopaage so we loss units ihe trial** 
7. **in reworking, we record these data, number of pallets that being reworked and every pallet have custom number of articles so if we have 2 pallets and number of article per pallet 48 so we rework for 96 unit, these 96 unit after rework some of them can moved to cullet, some in Hold and the rest in Resorted. given that reworking quantity is a subset of total molten units produced from that order**
8. **in general we measure our losses in our factory from 2 point of views losses in time and losses in defects**
9. **for time losses, we have losses in job change type that can classified to smaal change or medium change or big change or process change, we relate that losses to every job order that is produce custome product code in custom shift at custom machine,**

   1. **Trial losses : Time spent on trial runs before stable production**
   2. **T1 lossess (Mechanical/Setup) : Time lost during mechanical work and setup**
   3. **T2 Losses (Forming/Process) : Time lost during forming process adjustment**
   4. **CE Losses (Cold End) : Time lost at the cold end (inspection, packing area)**
   5. **Palletizer Losses : Time lost at the palletizing/packing station**
   6. **HE Breakdown Losses : Hot End machine breakdown time**
   7. **Extra T1 Losses : Additional unplanned setup time beyond T1 target**
   8. **Extra T2 Losses : Additional unplanned forming time beyond T2 target**
   9. **Total Job Change Losses : SUM of ALL losses combined**
10. **for defect losses, we cateogrise defects names to 3 main categories critical, major, minor. every defect name can be only major or minor or critical, where as we record qty for every defect appeared whther in normal production, trail, reworking case. with resposect to which order and product code also for rejections we have multiple rejection zones splitter to whther in hot end or cold end zone and every zone splitted to other cateogres that appeared in it** 


|\| # \| Category \| Column Name \| What It Measures \| Loss Type \|<br />\|:---:\|:---\|:---\|:---\|:---\|<br />\| 1 \| Production Input \| Actual Pack \| Total pieces packed \| Baseline \|<br />\| 2 \| Hot End Defects \| HE Conv. \| Hot End conveyor losses \| Quality Loss \|<br />\| 2 \| Hot End Defects \| HE Losses \| Hot End breakdowns \| Time Loss \|<br />\| 2 \| Hot End Defects \| HE Reject \| Hot End rejections \| Quality Loss \|<br />\| 3 \| Lehr Zone \| Lehr Entry \| Pieces entering lehr \| Baseline \|<br />\| 3 \| Lehr Zone \| Lehr Losses \| Breakage in annealing \| Quality Loss \|<br />\| 3 \| Lehr Zone \| Lehr Pack \| Pieces leaving lehr \| Baseline \|<br />\| 4 \| Cold End \| CE Entry \| Cold End entry \| Baseline \|<br />\| 4 \| Cold End \| CE Losses \| Cold End breakdowns \| Time Loss \|<br />\| 4 \| Cold End \| MNR Losses \| Manual rejects \| Quality Loss \|<br />\| 5 \| IS Machine (Forming) \| Section 01-10 \| Defects per section \| Quality Loss \|<br />\| 5 \| IS Machine (Forming) \| Total Section Stops \| Machine stops \| Time Loss \|<br />\| 5 \| IS Machine (Forming) \| Stuck \& Down \| Machine downtime \| Time Loss \|<br />\| 6 \| Quality Categories \| Total Reject \| Total rejected pieces \| Quality Loss \|<br />\| 6 \| Quality Categories \| Total Resort \| Reworked pieces \| Quality/Time Loss \|<br />\| 6 \| Quality Categories \| Total Hold \| Held for inspection \| Quality/Time Loss \|<br />\| 6 \| Quality Categories \| Visual \| Visual inspection fails \| Quality Loss \|<br />\| 7 \| Secondary Losses \| Gob Cuts \| Gob weight issues \| Quality Loss \|<br />\| 7 \| Secondary Losses \| Pallet In \| Palletizer issues \| Time Loss \|<br />\| 7 \| Secondary Losses \| Total EVO12/16/5 \| Specific defect codes \| Quality Loss \|<br />\| 7 \| Secondary Losses \| Total SanLi \| Specific defect codes \| Quality Loss \||
|-|







