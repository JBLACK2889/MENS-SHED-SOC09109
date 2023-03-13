import sqlite3

conn = sqlite3.connect('Database.db')

c = conn.cursor()

tools_data =[
(1,'Titan Cordless Drill Standard & Masonary','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0010.JPG',True,True,False),
(2,'Titan SDS Drill & Bits','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0008.JPG',True,True,False),
(3,'Hilti SF180A Cordless Drill Standard & Masonary','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0009.JPG',True,True,False),
(4,'B&D Corded Drill','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0017.JPG',True,True,False),
(5,'Unbranded Cordless Drill','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0016.JPG',True,True,False),
(6,'B&D Handheld Saw 18v Cordless','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0015.JPG',True,True,False),
(7,'Wolf Handheld Saw','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0014.JPG',True,True,False),
(8,'Wolf Saphire Handheld Saw','Portable Electric Handtools','On/Off switch does not meet regs','NULL','NULL','2022/07/15','	',True,True,False),
(9,'Erbouer Handheld Saw','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0013.JPG',True,True,False),
(10,'Clarke Corded Multitool Cutter','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0019.JPG',True,True,False),
(11,'B&D Corded Powered Hacksaw','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0034.JPG',True,True,False),
(12,'Pro Corded Jigsaw','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0021.JPG',True,True,False),
(13,'Bosch Corded Jigsaw','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0020.JPG',True,True,False),
(14,'Evolution Corded Jigsaw','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0022.JPG',True,True,False),
(15,'Erbouer Router','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0033.JPG',True,True,False),
(16,'Pro Belt Sander','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0032.JPG',True,True,True),
(17,'Parkside Belt sander','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0031.JPG',True,True,True),
(18,'B&D Belt Sander','Portable Electric Handtools','good','NULL','NULL','2022/07/15','	',True,True,True),
(19,'Erbouer Orbital Sander','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0011.JPG',True,True,False),
(20,'Einhell Chainsaw','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0039.JPG',True,True,True),
(21,'Workzone 12v Rotary Tool','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0036.JPG',True,True,False),
(22,'B&D Powered Screwdriver ?','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0038.JPG',False,False,False),
(23,'Bosch Heat Gun','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0035.JPG',False,False,False),
(24,'Parkside Hot Glue Gun','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0037.JPG',False,False,False),
(25,'Titan Wallpaper Stripper','Portable Electric Handtools','needs attention','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0026.JPG',False,False,False),
(26,'Battery Charger','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0028.JPG',False,False,False),
(27,'Parker Invertor Arc Welder','Portable Electric Handtools','good','NULL','NULL','2022/07/15','	',True,True,True),
(28,'Parkside Angle Grinder','Portable Electric Handtools','good','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0025.JPG',True,True,False),
(29,'Unbranded Angle Grinder','Portable Electric Handtools','Cable repair required','NULL','NULL','2022/07/15','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0023.JPG',True,True,False),
(30,'Tyme Machines, The Cub, Wood lathe','Benchtop Fixed Plant Machinery','good','NULL','GMS','2022/07/18','	',True,True,True),
(31,'Clarke Woodworker, Wood Lathe','Benchtop Fixed Plant Machinery','Not commissioned','NULL','GMS','2022/07/18','	',True,True,True),
(32,'Unbranded Wood Lathe','Benchtop Fixed Plant Machinery','Not commissioned','NULL','GMS','2022/07/18','	',True,True,True),
(33,'Unbranded Wood Lathe + Tools','Benchtop Fixed Plant Machinery','Not commissioned','NULL','GR','2022/07/18','	',True,True,True),
(34,'SIP 10" Table Saw','Benchtop Fixed Plant Machinery','needs attention','NULL','GR','2022/07/18','	',True,True,False),
(35,'Erbauer Cross Cut Mitre Saw','Benchtop Fixed Plant Machinery','Broken Guard','NULL','NULL','2022/07/18','	',True,True,False),
(36,'Sealey Pillar Drill','Benchtop Fixed Plant Machinery','Safety Cut Off ?','NULL','FC','2022/07/18','	',True,True,False),
(37,'Silverline 350w Drill Press','Benchtop Fixed Plant Machinery','Not Working','NULL','NULL','2022/07/18','	',True,True,False),
(38,'Clarke Woodworker Belt & Disc Sander','Benchtop Fixed Plant Machinery','needs attention','NULL','NULL','2022/07/18','	',True,True,False),
(39,'P Performance BSW Scroll Saw','Benchtop Fixed Plant Machinery','needs attention','NULL','NULL','2022/07/18','	',True,True,False),
(40,'P Performance Powe 150mm Bench grinder & Sander','Benchtop Fixed Plant Machinery','needs attention','NULL','NULL','2022/07/18','	',True,True,False),
(41,'Sealey Bench Grinder','Benchtop Fixed Plant Machinery','needs attention','NULL','NULL','2022/07/18','	',True,True,False),
(42,'Parkside Bench Grinder','Benchtop Fixed Plant Machinery','needs attention','NULL','NULL','2022/07/18','	',True,True,False),
(43,'P Performance 125mm Bench Grinder','Benchtop Fixed Plant Machinery','needs attention','NULL','NULL','2022/07/18','	',True,True,False),
(44,'Bosch Router & Table/Bench POF 400 ','Benchtop Fixed Plant Machinery','needs attention','NULL','NULL','2022/07/18','	',True,True,False),
(45,'MAC ALLISTER Router & Table/Bench','Benchtop Fixed Plant Machinery','needs attention','NULL','NULL','2022/07/18','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0040.JPG',True,False,False),
(46,'Axminster Model Engineer Metalwork Lathe','Benchtop Fixed Plant Machinery','good','NULL','NULL','2022/07/18','	',True,True,True),
(47,'Industrial Vacuum Cleaner','Miscellaneous','good','NULL','NULL','2022/07/18','	',False,False,False),
(48,'3 Trail Lights','Miscellaneous','good','NULL','NULL','2022/07/18','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0027.JPG',False,False,False),
(49,'Qualcast Garden Strimmer','Miscellaneous','good','NULL','NULL','2022/07/18','	',False,False,False),
(50,'Extention Lead','Miscellaneous','good','NULL','NULL','2022/07/18','https://github.com/JBLACK2889/MENS-SHED-SOC09109/blob/main/Equipment%20July%2022/IMG_0029.JPG',False,False,False),
]

c.executemany("INSERT INTO Tools VALUES (?,?,?,?,?,?,?,?,?,?,?)", tools_data)

conn.commit()
conn.close()
