from eink import EInk
from datetime import datetime
eink = EInk()

mydatetime = datetime.now().replace(hour =12, minute =0)
eink.send_localtime(mydatetime)


eink.send_start()
eink.send_meeting(0,"9:15 AM - 9:45 AM , backlog scrub; Conf Rm - Reston, VA, 8th Floor - Nexen (8)")
eink.send_meeting(1,"10:45 AM - 11:15 AM , ESPIR Unified Standup Vol. 2; Same room ENDPOINT / UAC uses")
eink.send_meeting(2,"10:45 AM - 11:00 AM , Endpoint Standup; Conf Rm - Reston, VA, 8th Floor - New York Times (8)")
eink.send_meeting(3,"11:15 AM - 11:45 AM , project planning")
eink.send_meeting(4,"12:30 PM - 1:30 PM , 1:1")
eink.send_meeting(5,"1:30 PM - 2:30 PM , Drew/Chris 1:1; 8")
eink.send_meeting(6,"2:30 PM - 3:00 PM , ESPIR weekly project meeting; Conf Rm - Reston, VA, 8th Floor - Brocade (10)")
eink.send_meeting(7,"3:30 PM - 4:00 PM , Machine Learning in MD; Conf Rm - Reston, VA, 8th Floor - New York Times (8)")
eink.send_meeting(8,"4:00 PM - 5:00 PM , ESPIR desk scrub; Conf Rm - Reston, VA, 8th Floor - New York Times (8)")
eink.send_meeting(9,"4:00 PM - 4:45 PM , Weekly Helix + Cloud Srvcs Program meeting; Conf Rm - 601 - U1L - Bespin (8 - 12)")
eink.send_todo(0, "Proper Preparation Prevents Poor...")
eink.send_todo(1, "dates need to be in UTC")
eink.send_todo(2, "add created time to agent tasks")
eink.send_todo(3, "remove limit from agent tables e...")
eink.send_todo(4, "remove need to unify task result...")
eink.send_todo(5, "add loading mask to acquisition ...")
eink.send_todo(6, "check if sb works on incident pa...")
eink.send_todo(7, "new task api needs to display er...")
eink.send_todo(8, "check with anthony - audits used...")
eink.send_todo(9, "verify modal pops up everywhere")
eink.send_todo(10, "add md5 click action back into a...")
eink.send_weather(0, "2:00 AM", "Showers", mydatetime)

eink.send_flush()