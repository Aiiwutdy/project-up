import turtle
from tkinter import *
from tkinter import messagebox
import tltk


App = Tk()
App.title('การพัฒนาต้นแบบความเข้าใจภาษาไทยโดยใช้ทฤษฎีการแปลความหมายโดยตรงจากจินตภาพ')
# root.config(bg='#80c1ff')
App.geometry('1360x768+400+50')
App.resizable(False, False)

img = PhotoImage(file='bg2_1.png')  # นำพื้นหลังเข้ามา
backgrounb = Label(App, image=img)  # กำหนดพื้นหลังให้อยู่ในหน้าต่างโปรแกรม
backgrounb.pack(side=TOP)
All_Vocab = PhotoImage(file='All_Cab_2.png')

sentence_lmd = [['จาน', ['z', 'x', 'p', 'q', 'n']], ['มีด', ['z', 'x', 'p', 'q', 'n']],
                ['ตู้', ['z', 'x', 'p', 'q', 'n']], ['แจกัน', ['z', 'x', 'p', 'q', 'n']],
                ['แก้วน้ำ', ['z', 'x', 'p', 'q', 'n']], ['แว่นตา', ['z', 'x', 'p', 'q', 'n']],
                ['แหวน', ['z', 'x', 'p', 'q', 'n']], ['ลูกโป่ง', ['z', 'x', 'p', 'q', 'n']],
                ['ดินสอ', ['z', 'x', 'p', 'q', 'n']], ['รองเท้า', ['z', 'x', 'p', 'q', 'n']],
                ['ดอกไม้', ['z', 'x', 'p', 'q', 'n']], ['ช้อน', ['z', 'x', 'p', 'q', 'n']],
                ['นาฬิกา', ['z', 'x', 'p', 'q', 'n']], ['หนังสือ', ['z', 'x', 'p', 'q', 'n']],
                ['ปืน', ['z', 'x', 'p', 'q', 'n']], ['ขวด', ['z', 'x', 'p', 'q', 'n']],
                ['ตะหลิว', ['z', 'x', 'p', 'q', 'n']], ['กระทะ', ['z', 'x', 'p', 'q', 'n']],
                ['หวี', ['z', 'x', 'p', 'q', 'n']], ['ตู้เย็น', ['z', 'x', 'p', 'q', 'n']],
                ['เข็มขัด', ['z', 'x', 'p', 'q', 'n']], ['สมุด', ['z', 'x', 'p', 'q', 'n']],
                ['พัดลม', ['z', 'x', 'p', 'q', 'n']], ['ลูกบอล', ['z', 'x', 'p', 'q', 'n']],
                ['เตารีด', ['z', 'x', 'p', 'q', 'n']], ['ไม้กวาด', ['z', 'x', 'p', 'q', 'n']],
                ['วิทยุ', ['z', 'x', 'p', 'q', 'n']], ['กล่อง', ['z', 'x', 'p', 'q', 'n']],
                ['โต๊ะ', ['z', 'x', 'p', 'q', 'n']], ['โรงเรียน', ['z', 'x', 'p', 'q', 'n']],
                ['กา', ['x', 'x', 'p', 'q', 'n']], ['ป่า', ['z', 'x', 'p', 'q', 'n']],
                ['สุนัข', ['x', 'x', 'p', 'q', 'n']], ['บ้าน', ['z', 'x', 'p', 'q', 'n']],
                ['ลา', ['x', 'x', 'p', 'q', 'n']], ['ปาก', ['z', 'x', 'p', 'q', 'n']],
                ['ถาด', ['z', 'x', 'p', 'q', 'n']], ['ว่าว', ['z', 'x', 'p', 'q', 'n']],
                ['ปลา', ['x', 'x', 'p', 'q', 'n']], ['นาข้าว', ['z', 'x', 'p', 'q', 'n']],
                ['ผ้า', ['z', 'x', 'p', 'q', 'n']], ['หน้าต่าง', ['z', 'x', 'p', 'q', 'n']],
                ['ช้าง', ['x', 'x', 'p', 'q', 'n']], ['ม้า', ['x', 'x', 'p', 'q', 'n']],
                ['ขา', ['z', 'x', 'p', 'q', 'n']], ['ดาว', ['z', 'x', 'p', 'q', 'n']],
                ['พาน', ['z', 'x', 'p', 'q', 'n']], ['ควาย', ['x', 'x', 'p', 'q', 'n']],
                ['คีม', ['z', 'x', 'p', 'q', 'n']], ['หีบ', ['z', 'x', 'p', 'q', 'n']],
                ['ปู', ['x', 'x', 'p', 'q', 'n']], ['หนู', ['x', 'x', 'p', 'q', 'n']],
                ['งู', ['x', 'x', 'p', 'q', 'n']], ['ครู', ['x', 'x', 'p', 'q', 'n']],
                ['ปลาทู', ['z', 'x', 'p', 'q', 'n']], ['ปูม้า', ['x', 'x', 'p', 'q', 'n']],
                ['ธูป', ['z', 'x', 'p', 'q', 'n']], ['เทียน', ['z', 'x', 'p', 'q', 'n']],
                ['เมฆ', ['z', 'x', 'p', 'q', 'n']], ['ผู้หญิง', ['x', 'x', 'p', 'q', 'n']],
                ['ผู้ชาย', ['x', 'x', 'p', 'q', 'n']], ['ทะเล', ['z', 'x', 'p', 'q', 'n']],
                ['ของเล่น', ['z', 'x', 'p', 'q', 'n']], ['จระเข้', ['x', 'x', 'p', 'q', 'n']],
                ['เม่น', ['x', 'x', 'p', 'q', 'n']], ['เข่ง', ['z', 'x', 'p', 'q', 'n']],
                ['เค้ก', ['z', 'x', 'p', 'q', 'n']], ['กางเกง', ['z', 'x', 'p', 'q', 'n']],
                ['กวาง', ['x', 'x', 'p', 'q', 'n']], ['แมว', ['x', 'x', 'p', 'q', 'n']],
                ['แมงมุม', ['x', 'x', 'p', 'q', 'n']], ['แตงโม', ['z', 'x', 'p', 'q', 'n']],
                ['แปรงฟัน', ['z', 'x', 'p', 'q', 'n']], ['ข้าวโพด', ['z', 'x', 'p', 'q', 'n']],
                ['โคมไฟ', ['z', 'x', 'p', 'q', 'n']], ['สิงโต', ['x', 'x', 'p', 'q', 'n']],
                ['โอ่ง', ['z', 'x', 'p', 'q', 'n']], ['โซ่', ['z', 'x', 'p', 'q', 'n']],
                ['หมอน', ['z', 'x', 'p', 'q', 'n']], ['มะละกอ', ['z', 'x', 'p', 'q', 'n']],
                ['หม้อ', ['z', 'x', 'p', 'q', 'n']], ['ตระกร้อ', ['z', 'x', 'p', 'q', 'n']],
                ['กอไผ่', ['z', 'x', 'p', 'q', 'n']], ['หอย', ['x', 'x', 'p', 'q', 'n']],
                ['กล้อง', ['z', 'x', 'p', 'q', 'n']], ['มังคุด', ['z', 'x', 'p', 'q', 'n']],
                ['ทุเรียน', ['z', 'x', 'p', 'q', 'n']], ['ตุ้มหู', ['z', 'x', 'p', 'q', 'n']],
                ['ทุ่งนา', ['z', 'x', 'p', 'q', 'n']], ['นิ้ว', ['z', 'x', 'p', 'q', 'n']],
                ['ลิง', ['x', 'x', 'p', 'q', 'n']], ['จิงโจ้', ['x', 'x', 'p', 'q', 'n']],
                ['ดอกมะลิ', ['z', 'x', 'p', 'q', 'n']], ['ลิเก', ['z', 'x', 'p', 'q', 'n']],
                ['กิ้งก่า', ['x', 'x', 'p', 'q', 'n']], ['กะทิ', ['z', 'x', 'p', 'q', 'n']],
                ['หิ้งห้อย', ['x', 'x', 'p', 'q', 'n']], ['ชิงช้า', ['z', 'x', 'p', 'q', 'n']],
                ['กิ่งไม้', ['z', 'x', 'p', 'q', 'n']], ['ฉิ่ง', ['z', 'x', 'p', 'q', 'n']],
                ['ก้อนหิน', ['z', 'x', 'p', 'q', 'n']], ['ต้นไม้', ['z', 'x', 'p', 'q', 'n']],
                ['ไห', ['z', 'x', 'p', 'q', 'n']], ['สบู่', ['z', 'x', 'p', 'q', 'n']],
                ['มือ', ['z', 'x', 'p', 'q', 'n']], ['กำไล', ['z', 'x', 'p', 'q', 'n']],
                ['ส้มตำ', ['z', 'x', 'p', 'q', 'n']], ['ภูเขา', ['z', 'x', 'p', 'q', 'n']],
                ['เตาไฟ', ['z', 'x', 'p', 'q', 'n']], ['เต่า', ['x', 'x', 'p', 'q', 'n']],
                ['เล้าไก่', ['z', 'x', 'p', 'q', 'n']], ['ไข่เจียว', ['z', 'x', 'p', 'q', 'n']],
                ['ไก่แจ้', ['x', 'x', 'p', 'q', 'n']], ['ตะเกียบ', ['z', 'x', 'p', 'q', 'n']],
                ['เตียงนอน', ['z', 'x', 'p', 'q', 'n']], ['เกวียน', ['z', 'x', 'p', 'q', 'n']],
                ['เคียว', ['z', 'x', 'p', 'q', 'n']], ['เกลือ', ['z', 'x', 'p', 'q', 'n']],
                ['มะเขือ', ['z', 'x', 'p', 'q', 'n']], ['เสื้อผ้า', ['z', 'x', 'p', 'q', 'n']],
                ['เหยือกน้ำ', ['z', 'x', 'p', 'q', 'n']], ['นางเงือก', ['x', 'x', 'p', 'q', 'n']],
                ['มะเฟือง', ['z', 'x', 'p', 'q', 'n']], ['เสือ', ['x', 'x', 'p', 'q', 'n']],
                ['เรือ', ['z', 'x', 'p', 'q', 'n']], ['เสื่อ', ['z', 'x', 'p', 'q', 'n']],
                ['ใบบัว', ['z', 'x', 'p', 'q', 'n']], ['รั้ว', ['z', 'x', 'p', 'q', 'n']],
                ['หนอน', ['x', 'x', 'p', 'q', 'n']], ['มะม่วง', ['z', 'x', 'p', 'q', 'n']],
                ['หมวก', ['z', 'x', 'p', 'q', 'n']], ['กล้วย', ['z', 'x', 'p', 'q', 'n']],
                ['วัด', ['z', 'x', 'p', 'q', 'n']], ['กะละมัง', ['z', 'x', 'p', 'q', 'n']],
                ['กระต่าย', ['x', 'x', 'p', 'q', 'n']], ['มะไฟ', ['z', 'x', 'p', 'q', 'n']],
                ['มะพร้าว', ['z', 'x', 'p', 'q', 'n']], ['มะกรูด', ['z', 'x', 'p', 'q', 'n']],
                ['มะระ', ['z', 'x', 'p', 'q', 'n']], ['กะลา', ['z', 'x', 'p', 'q', 'n']],
                ['กะปิ', ['z', 'x', 'p', 'q', 'n']], ['กระเช้า', ['z', 'x', 'p', 'q', 'n']],
                ['กระบุง', ['z', 'x', 'p', 'q', 'n']], ['ไข่', ['z', 'x', 'p', 'q', 'n']],
                ['เป็ด', ['x', 'x', 'p', 'q', 'n']], ['เบ็ด', ['z', 'x', 'p', 'q', 'n']],
                ['เห็ด', ['z', 'x', 'p', 'q', 'n']], ['ดอกเข็ม', ['z', 'x', 'p', 'q', 'n']],
                ['รถเข็น', ['z', 'x', 'p', 'q', 'n']], ['แกะ', ['x', 'x', 'p', 'q', 'n']],
                ['รถ', ['z', 'x', 'p', 'q', 'n']], ['ร่ม', ['z', 'x', 'p', 'q', 'n']],
                ['กรง', ['z', 'x', 'p', 'q', 'n']], ['ผ้าห่ม', ['z', 'x', 'p', 'q', 'n']],
                ['เก้าอี้', ['z', 'x', 'p', 'q', 'n']], ['ผีเสื้อ', ['x', 'x', 'p', 'q', 'n']],
                ['เมือง', ['z', 'x', 'p', 'q', 'n']], ['วัง', ['z', 'x', 'p', 'q', 'n']],
                ['ชาม', ['z', 'x', 'p', 'q', 'n']], ['ถัง', ['z', 'x', 'p', 'q', 'n']],
                ['สนาม', ['z', 'x', 'p', 'q', 'n']], ['โคมไฟ', ['z', 'x', 'p', 'q', 'n']],
                ['ขนม', ['z', 'x', 'p', 'q', 'n']], ['มะขาม', ['z', 'x', 'p', 'q', 'n']],
                ['ข้าวหลาม', ['z', 'x', 'p', 'q', 'n']], ['ชมพู่', ['z', 'x', 'p', 'q', 'n']],
                ['ถ้วย', ['z', 'x', 'p', 'q', 'n']], ['ขลุ่ย', ['z', 'x', 'p', 'q', 'n']],
                ['อ้อย', ['z', 'x', 'p', 'q', 'n']], ['ลิ้นจี่', ['z', 'x', 'p', 'q', 'n']],
                ['ลูกชิ้น', ['z', 'x', 'p', 'q', 'n']], ['ถนน', ['z', 'x', 'p', 'q', 'n']],
                ['ของขวัญ', ['z', 'x', 'p', 'q', 'n']], ['คุกกี้', ['z', 'x', 'p', 'q', 'n']],
                ['ผัก', ['z', 'x', 'p', 'q', 'n']], ['ครก', ['z', 'x', 'p', 'q', 'n']],
                ['จอบ', ['z', 'x', 'p', 'q', 'n']], ['ฉาบ', ['z', 'x', 'p', 'q', 'n']],
                ['กรอบรูป', ['z', 'x', 'p', 'q', 'n']], ['ทัพพี', ['z', 'x', 'p', 'q', 'n']],
                ['มด', ['x', 'x', 'p', 'q', 'n']], ['จรวด', ['z', 'x', 'p', 'q', 'n']],
                ['ตลาด', ['z', 'x', 'p', 'q', 'n']], ['อิฐ', ['z', 'x', 'p', 'q', 'n']],
                ['กบ', ['x', 'x', 'p', 'q', 'n']], ['ปลาทอง', ['z', 'x', 'p', 'q', 'n']],
                ['ไส้กรอก', ['z', 'x', 'p', 'q', 'n']], ['นม', ['z', 'x', 'p', 'q', 'n']],
                ['หน่อไม้', ['z', 'x', 'p', 'q', 'n']], ['หลังคา', ['z', 'x', 'p', 'q', 'n']],
                ['ถ้ำ', ['z', 'x', 'p', 'q', 'n']], ['กลอง', ['z', 'x', 'p', 'q', 'n']],
                ['เสื้อ', ['z', 'x', 'p', 'q', 'n']], ['เตาแก๊ส', ['z', 'x', 'p', 'q', 'n']],
                ['เต่าทอง', ['x', 'x', 'p', 'q', 'n']], ['เต้าหู้', ['z', 'x', 'p', 'q', 'n']],
                ['ทอง', ['z', 'x', 'p', 'q', 'n']], ['กระรอก', ['x', 'x', 'p', 'q', 'n']],
                ['จดหมาย', ['z', 'x', 'p', 'q', 'n']], ['ผลไม้', ['ผ', 'x', 'p', 'q', 'n']],
                ['ห้องสมุด', ['z', 'x', 'p', 'q', 'n']], ['ห้องพยาบาล', ['z', 'x', 'p', 'q', 'n']],
                ['พ่อค้า', ['x', 'x', 'p', 'q', 'n']], ['พระ', ['x', 'x', 'p', 'q', 'n']],
                ['ป้า', ['x', 'x', 'p', 'q', 'n']], ['แม่', ['x', 'x', 'p', 'q', 'n']],
                ['เกษตรกร', ['x', 'x', 'p', 'q', 'n']], ['ยาย', ['x', 'x', 'p', 'q', 'n']],
                ['ปู่', ['x', 'x', 'p', 'q', 'n']], ['พี่สาว', ['x', 'x', 'p', 'q', 'n']],
                ['นักเรียน', ['x', 'x', 'p', 'q', 'n']], ['ตำรวจ', ['x', 'x', 'p', 'q', 'n']],
                ['นักมวย', ['x', 'x', 'p', 'q', 'n']], ['ชาวสวน', ['x', 'x', 'p', 'q', 'n']],
                ['แม่ครัว', ['x', 'x', 'p', 'q', 'n']], ['รั้วบ้าน', ['z', 'x', 'p', 'q', 'n']],
                ['ส้อม', ['z', 'x', 'p', 'q', 'n']], ['ไก่', ['x', 'x', 'p', 'q', 'n']],
                ['ปากกา', ['z', 'x', 'p', 'q', 'n']], ['พี่ชาย', ['x', 'x', 'p', 'q', 'n']],
                ['สีแดง', ['z', 'x', 'p', 'q', 'n']], ['สีฟ้า', ['x', 'x', 'p', 'q', 'n']],
                ['สีเหลือง', ['z', 'x', 'p', 'q', 'n']], ['สีขาว', ['x', 'x', 'p', 'q', 'n']],
                ['เรา', ['x', 'x', 'p', 'q', 'pn']], ['เธอ', ['x', 'x', 'p', 'q', 'pn']],
                ['ฉัน', ['x', 'x', 'p', 'q', 'pn']], ['มา', ['x', 'x', 'q', 'p', 'v']],
                ['ถือ', ['x', 'y', 'z', 'x', 'v']], ['หยิบ', ['x', 'y', 'z', 'x', 'v']],
                ['จับ', ['x', 'y', 'z', 'x', 'v']], ['อยู่', ['x', 'y', 'x', 'x', 'adv']],
                ['วาง', ['x', 'x', 'p', 'q', 'v']], ['ที่', ['x', 'x', 'y', 'x', 'pp']],
                ['ใน', ['x', 'x', 'y', 'x', 'pp']], ['บน', ['x', 'x', 'y', 'x', 'pp']],
                ['ใต้', ['x', 'x', 'x', 'y', 'pp']], ['ไป', ['x', 'x', 'p', 'q', 'v']],
                ['ทาสี', ['x', 'y', 'p', 'q', 'v']], ['รั้วโรงเรียน', ['z', 'x', 'p', 'q', 'n']],
                ['ปีน', [['x', 'x', 'p', 'q', 'v'], 'SAND', ['x', 'x', 'up', 'up', 'v'],
                         'SAND', ['x', 'x', 'y', 'y', 'v']]],
                ['โยน', [['x', 'y', 'hand', 'hand', 'v'], 'SAND', ['x', 'hand', 'p', 'q', 'v'],
                         'CAND', ['x', 'y', 'hand', 'air', 'v']]],
                ['ให้', [['x', 'z', 'x', 'y', 'v'], 'SAND', ['y', 'z', 'x', 'y', 'v']]]]



def run(sen):
    test = sen  # ประโยคที่ใช้ทดสอบ
    test = tltk.nlp.word_segment(test)  # ตัดคำ
    test = test.replace("<s/>", "")  # เอา</s>ออกจากประโยค
    print("แบ่งประโยค : ", test)
    return sentolist(test)


# ทำให้ประโยคจากการตัดคำกลายเป็นlist
def sentolist(test):
    stat = 0
    end = 0
    test_it = []
    for i in range(len(test)):
        if test[i] == "|":
            end = i
            test_it.append(test[stat:end])
            stat = i + 1
    test_it.append(test[stat:len(test)])
    result = test_it
    result.pop()
    for count in range(len(result)):
        c = count
    print('ก่อนแก้', result)
    if c == 1:
        if result[1] == 'ที่อยู่':
            del result[1]
        elif result[1] == 'ใต้โต๊ะ':
            result.pop()
            result.append('ใต้')
            result.append('โต๊ะ')
        elif result[0] == 'ฉันทา':
            # result.clear()
            result = ['ฉัน', 'ทาสี']
    elif c == 2:
        if result[2] == 'ที่อยู่':
            del result[2]
        elif result[2] == 'ใต้โต๊ะ':
            result.pop()
            result.append('ใต้')
            result.append('โต๊ะ')
        elif result[0] == 'ฉันทา':
            del result[0]
            result.insert(0, 'ฉัน')
            result.insert(1, 'ทาสี')
            if result[2] == 'สี':
                del result[2]
        elif result[1] == 'ทาสี':
            result.insert(2, 'สี' + result[2])
            if result[2] == 'สี' + result[3]:
                del result[2]
                if result[2] != 'สี' + result[2]:
                    result.insert(2, 'สี' + result[2])
                    del result[3]
    elif c == 3:  # ฉันทาสีแดงที่รั้ว แม่ทาสีแดงที่รั้ว
        if result[3] == 'ที่อยู่':
            del result[3]
        if result[3] == 'ใต้โต๊ะ':
            result.pop()
            result.append('ใต้')
            result.append('โต๊ะ')
        if result[0] == 'ฉันทา':
            result.insert(2, result[1])
            del result[0:2]
            result.insert(0, 'ฉัน')
            result.insert(1, 'ทาสี')
            if result[2] == 'ห้อง':
                del result[2]
                result.insert(2, 'ห้อง' + result[2] + result[1])
                result.pop()
            elif result[2] == 'สี':
                del result[2]
        if result[1] == 'ทา':
            del result[1]
            result.insert(1, 'ทาสี')
        if result[2] == 'รั้ว':
            if result[3] == 'บ้าน':
                del result[2:4]
                result.insert(2, 'รั้วบ้าน')
            elif result[3] == 'โรงเรียน':
                del result[2:4]
                result.insert(2, 'รั้วโรงเรียน')
    elif c == 4:
        if result[0] == 'ฉันทา':
            del result[0:2]
            result.insert(0, 'ฉัน')
            result.insert(1, 'ทาสี')
        if result[1] == 'ทาสี':  # แก้แม่ทาสีแดงที่บ้าน
            result.insert(2, 'สี' + result[2])
            del result[3]
    # print(type(result))
    print("แบ่งคำลงใน List : ", result)
    print("หลังแก้", result)
    return check_Vocab(result)

def check_Vocab(result):
    word = []
    sentence = []
    for i in range(len(result)):
        for ii in range(len(sentence_lmd)):
            if result[i] == sentence_lmd[ii][0]:
                word.append(sentence_lmd[ii][0])
    for c in range(len(result)):
        count_c = c
    for cc in range(len(word)):
        count_cc = cc
    if c == cc:
        print("คำที่มีในระบบ : ", word)
        sentence.append(word)
        return To_Lmd_Expression(sentence)
    elif c != cc:
        # print("บางคำไม่ได้อยู่ในระบบ")
        messeage_alert()

def messeage_alert():
    messagebox.showinfo(title='แจ้งเตือน!!!', message='ไม่พบคำในระบบ')

def popup_alert():
    messagebox.showinfo(title='แจ้งเตือน!!!', message='ประโยคนี้ไม่สามารถแสดงรูปภาพได้')

def To_Lmd_Expression(sentence):

    temp = []
    temp1 = []
    temp2 = []
    # print(sentence)
    #### ตัดคำที่ไม่จำเป็นออกจากประโยค ####
    for q in range(len(sentence[0])):
        count_q = q
        # print(count_q)
    if count_q == 4: #แม่ทาสีอยู่ในบ้าน เกิดERROR แม่ทาสีในบ้าน
        if sentence[0][1] == 'วาง' and sentence[0][2] == 'อยู่':
            del sentence[0][1:3]
            print("ตัดคำ : ", sentence)
        elif sentence[0][1] == 'อยู่' and (sentence[0][2] == 'ใน' or 'ที่' or 'บน' or 'ใต้'):
            del sentence[0][1:3]
            print("ตัดคำ : ", sentence)
        elif sentence[0][1] == 'ทาสี' and (sentence[0][3] == 'ใน' or 'ที่' or 'บน' or 'ใต้'):
            if sentence[0][2] == 'รั้ว' and sentence[0][4] == 'บ้าน':
                del sentence[0][2:5]
                sentence[0].append('รั้วบ้าน')
                print("ตัดคำ : ", sentence)
            elif sentence[0][2] == 'รั้ว' and sentence[0][4] == 'โรงเรียน':
                del sentence[0][2:5]
                sentence[0].append('รั้วโรงเรียน')
                print("ตัดคำ : ", sentence)
        if sentence[0][1] == 'ทาสี' and sentence[0][2] == 'สี':
            del sentence[0][2]
            print("ตัดคำ : ", sentence[0])
    elif count_q == 3:
        if (sentence[0][1] == 'วาง') and (sentence[0][2] == 'ใน'):
            del sentence[0][1]
            print("ตัดคำ : ", sentence)
        elif (sentence[0][1] == 'วาง') and (sentence[0][2] == 'ที่'):
            del sentence[0][1]
            print("ตัดคำ : ", sentence)
        elif (sentence[0][1] == 'วาง') and (sentence[0][2] == 'บน'):
            del sentence[0][1]
            print("ตัดคำ : ", sentence)
        elif (sentence[0][1] == 'วาง') and (sentence[0][2] == 'ใต้'):
            del sentence[0][1]
            print("ตัดคำ : ", sentence)
            # print('1')
        elif (sentence[0][1] == 'อยู่') and (sentence[0][2] == 'ใน'):
            del sentence[0][1]
            print("ตัดคำ : ", sentence)
        elif (sentence[0][1] == 'อยู่') and (sentence[0][2] == 'ที่'):
            del sentence[0][1]
            print("ตัดคำ : ", sentence)
        elif (sentence[0][1] == 'อยู่') and (sentence[0][2] == 'บน'):
            del sentence[0][1]
            print("ตัดคำ : ", sentence)
        elif (sentence[0][1] == 'อยู่') and (sentence[0][2] == 'ใต้'):
            del sentence[0][1]
            print("ตัดคำ : ", sentence)
            # print('2')
        elif (sentence[0][1] == 'ทาสี') and (
                (sentence[0][2] == 'ใน' or 'ที่' or 'บน' or 'ใต้') and (sentence[0][2] == '')):  #แม่ทาสีในบ้าน
            del sentence[0][2]
            print("ตัดคำ : ", sentence)
            # print('3')
    # print("ตัดคำ : ", sentence)
            # print('3')
    # print("ตัดคำ : ", sentence)

    ########## เข้ารูปภาษาเพื่อการอธิบายจินตภาพ #############
    for l in range(len(sentence[0])):
        temp.append(sentence[0][l])
    for ll in range(len(temp)):
        # print(temp[ll])
        for lll in range(len(sentence_lmd)):
            # print(sentence_lmd[lll])
            if sentence_lmd[lll][0] == temp[ll]:
                temp1.append(sentence_lmd[lll])

    print("LMD TEMP1 : ", temp1)
    j = 0
    temp3 = []

    ######## ลดรูปภาษาเพื่อการอธิบายจินตภาพ ##########
    for j in range(len(temp1)):
        # temp2.append(temp1[j])
        count_j = j
        # print(temp1[j], count_j)
    if count_j == 2:
        if ((temp1[1][1][4] == 'v') or (temp1[1][1][4] == 'adv')) and temp1[2][1][4] == 'n':  # VERB(กริยา) + NOUN(นาม)
            if temp1[1][1][4] == 'v' and temp1[1][0] == 'ไป':
                temp2 = [['x', 'x', 'p', temp1[2][0], 'v']]
                temp3.append(temp1[0])
                temp3 += temp2
                # print("temp3",temp3)
                temp2.clear()
                if temp3[0][1][4] == 'pn' and temp3[1][4] == 'v':
                    print("LMD : ", temp3)
                    temp2 = [[temp3[0][0], temp3[0][0], 'p', temp3[1][3], 'a']]
                elif temp3[0][1][4] == 'n' and temp3[1][4] == 'v':
                    print("LMD : ", temp3)
                    temp2 = [[temp3[0][0], temp3[0][0], 'p', temp3[1][3], 'a']]
            elif temp1[1][1][4] == 'v' and temp1[1][0] == 'มา':
                temp2 = [['x', 'x', temp1[2][0], 'p', 'v']]
                temp3.append(temp1[0])
                temp3 += temp2
                temp2.clear()
                if temp3[0][1][4] == 'pn' and temp3[1][4] == 'v':
                    print("LMD : ", temp3)
                    temp2 = [[temp3[0][0], temp3[0][0], temp3[1][2], 'p', 'a']]
                elif temp3[0][1][4] == 'n' and temp3[1][4] == 'v':
                    print("LMD : ", temp3)
                    temp2 = [[temp3[0][0], temp3[0][0], temp3[1][2], 'p', 'a']]
            elif temp1[1][1][4] == 'adv' and temp1[1][0] == 'อยู่':
                temp2 = [['x', temp1[2][0], 'x', 'x', 'v']]
                temp3.append(temp1[0])
                temp3 += temp2
                temp2.clear()
                if temp3[0][1][4] == 'pn' and temp3[1][4] == 'v':
                    print("LMD : ", temp3)
                    temp2 = [[temp3[0][0], temp3[1][1], temp3[0][0], temp3[0][0], 'a']]
                elif temp3[0][1][4] == 'n' and temp3[1][4] == 'v':
                    print("LMD : ", temp3)
                    temp2 = [[temp3[0][0], temp3[1][1], temp3[0][0], temp3[0][0], 'a']]
            elif temp1[1][1][4] == 'v' and ((temp1[1][0] == 'ถือ' or 'หยิบ' or 'จับ') and (temp1[1][0] != 'ทาสี')):
                temp2 = [['x', temp1[2][0], 'y', 'x', 'v']]
                temp3.append(temp1[0])
                temp3 += temp2
                temp2.clear()
                if temp3[0][1][4] == 'pn' and temp3[1][4] == 'v':
                    print("LMD : ", temp3)
                    temp2 = [[temp3[0][0], temp3[1][1], temp1[0][0], temp1[0][0], 'a']]
                elif temp3[0][1][4] == 'n' and temp3[1][4] == 'v':
                    print("LMD : ", temp3)
                    temp2 = [[temp3[0][0], temp3[1][1], temp1[0][0], temp1[0][0], 'a']]
            elif temp1[1][1][4] == 'v' and temp1[1][0] == 'ทาสี': #ฉันทาสีแดง
                temp2 = [['x', temp1[2][0], 'p', 'q', 'v']]
                temp3.append(temp1[0])
                temp3 += temp2
                temp2.clear()
                print('temp3', temp3)
                if ((temp3[0][1][4] == 'pn') or (temp3[0][1][4] == 'n')) and temp3[1][1] == 'สีแดง':
                    temp2 = [[temp1[0][0], temp1[2][0], 'p', 'q', 'A32']]
                elif ((temp3[0][1][4] == 'pn') or (temp3[0][1][4] == 'n')) and temp3[1][1] == 'สีฟ้า':
                    temp2 = [[temp1[0][0], temp1[2][0], 'p', 'q', 'A32']]
                elif ((temp3[0][1][4] == 'pn') or (temp3[0][1][4] == 'n')) and temp3[1][1] == 'สีเหลือง':
                    temp2 = [[temp1[0][0], temp1[2][0], 'p', 'q', 'A32']]
                elif ((temp3[0][1][4] == 'pn') or (temp3[0][1][4] == 'n')) and temp3[1][1] == 'สีขาว':
                    temp2 = [[temp1[0][0], temp1[2][0], 'p', 'q', 'A32']]
                elif ((temp3[0][1][4] == 'pn') or (temp3[0][1][4] == 'n')) and temp3[1][4] == 'v':
                    temp2 = [[temp1[0][0], 'y', 'p', temp1[2][0], 'A32']]
        elif temp1[1][1][4] == 'pp' and temp1[2][1][4] == 'n':
            if temp1[1][1][4] == 'pp' and ((temp1[1][0] == 'ใน' or 'ที่' or 'บน') and temp1[1][0] != 'ใต้'):
                temp2 = [[temp1[1][0], temp1[1][0], temp1[2][0], temp1[0][0], 'v']]
                temp3 = [temp1[0]] + temp2
                temp2.clear()
                print('temp3 :', temp3)
                if temp3[0][1][4] == 'n' and temp3[1][4] == 'v':
                    temp2 = [[temp3[0][0], temp3[0][0], temp3[1][2], temp3[1][2], 'a'], ['SAND'], temp3[1]]
                elif temp3[0][1][4] == 'pn' and temp3[1][4] == 'v':
                    temp2 = [[temp3[0][0], temp3[0][0], temp3[1][2], temp3[1][2], 'a'], ['SAND'], temp3[1]]
            elif temp1[1][1][4] == 'pp' and temp1[1][0] == 'ใต้':
                temp2 = [[temp1[1][0], temp1[1][0], temp1[0][0], temp1[2][0], 'v']]
                temp3 = [temp1[0]] + temp2
                temp2.clear()
                print('temp3 :', temp3)
                if temp3[0][1][4] == 'n' and temp3[1][4] == 'v':
                    temp2 = [[temp3[0][0], temp3[0][0], temp3[1][3], temp3[1][3], 'a'], ['SAND'], temp3[1]]
                elif temp3[0][1][4] == 'pn' and temp3[1][4] == 'v':
                    temp2 = [[temp3[0][0], temp3[0][0], temp3[1][2], temp3[1][2], 'a'], ['SAND'], temp3[1]]
        elif temp1[1][0] == 'ปีน':
            if temp1[1][1][0][4] == 'v' and temp1[1][0] == 'ปีน':
                temp2 = [['x', 'x', 'p', 'q', 'a'], 'SAND', ['x', 'x', 'up', 'up', 'a'],
                         'SAND', ['x', 'x', temp1[2][0], temp1[2][0], 'a']]
                temp3.append(temp1[0])
                temp3 += temp2
                temp2.clear()
                print('temp3', temp3)
                if temp3[0][1][4] == 'pn' and temp3[1][4] == 'a':
                    temp2 = [[temp3[0][0], temp3[0][0], 'p', 'q', 'v'], 'SAND',
                             [temp3[0][0], temp3[0][0], 'up', 'up', 'A13'], 'SAND',
                             [temp3[0][0], temp3[0][0], temp1[2][0], temp1[2][0], 'v']]
                elif temp3[0][1][4] == 'n' and temp3[1][4] == 'a':
                    temp2 = [[temp3[0][0], temp3[0][0], 'p', 'q', 'v'], 'SAND',
                             [temp3[0][0], temp3[0][0], 'up', 'up', 'A13'], 'SAND',
                             [temp3[0][0], temp3[0][0], temp1[2][0], temp1[2][0], 'v']]
        elif temp1[1][0] == 'โยน':
            if temp1[1][1][0][4] == 'v' and temp1[1][0] == 'โยน':
                temp2 = [['x', temp1[2][0], 'hand', 'hand', 'v'], 'SAND', ['x', 'hand', 'p', 'q', 'v'],
                         'CAND', ['x', temp1[2][0], 'hand', 'air', 'v']]
                temp3.append(temp1[0])
                temp3 += temp2
                temp2.clear()
                print('temp3', temp3)
                if temp3[0][1][4] == 'pn' and temp3[1][4] == 'v':
                    temp2 = [[temp3[0][0], temp1[2][0], 'hand', 'hand', 'a'], 'SAND', [temp3[0][0], 'hand', 'p', 'q', 'a'],
                             'CAND', [temp3[0][0], temp1[2][0], 'hand', 'air', 'a']]
                elif temp3[0][1][4] == 'n' and temp3[1][4] == 'v':
                    temp2 = [[temp3[0][0], temp1[2][0], 'hand', 'hand', 'a'], 'SAND', [temp3[0][0], 'hand', 'p', 'q', 'a'],
                             'CAND', [temp3[0][0], temp1[2][0], 'hand', 'air', 'a']]
    elif count_j == 3: #ตัวอย่างประโยค ฉันให้ทองแม่ ฉันทาสีที่รั้ว
        if temp1[1][0] == 'ให้' and temp1[2][1][4] == 'n':
            if temp1[1][1][0][4] == 'v' and temp1[1][0] == 'ให้':
                temp2 = [['x', temp1[2][0], 'x', 'y', 'v'], 'SAND', ['y', temp1[2][0], 'x', 'y', 'v']]+[temp1[3]]
                temp3.append(temp1[0])
                temp3 += temp2
                temp2.clear()
                print('temp3', temp3)
                if temp3[1][4] == 'v' and temp3[4][1][4] == 'n':
                    temp2 = [['x', temp1[2][0], 'x', temp3[4][0], 'v'],
                             'SAND', [temp3[4][0], temp1[2][0], 'x', temp3[4][0], 'v']]
                    temp3.clear()
                    temp3.append(temp1[0])
                    temp3 += temp2
                    temp2.clear()
                    print('temp3', temp3)
                    if temp3[0][1][4] == 'pn' and temp3[1][4] == 'v':
                        temp2 = [[temp3[0][0], temp1[2][0], temp3[0][0], temp3[3][0], 'a'],
                                 'SAND', [temp3[3][0], temp1[2][0], temp3[0][0], temp3[3][0], 'a']]
                    elif temp3[0][1][4] == 'n' and temp3[1][4] == 'v':
                        temp2 = [[temp3[0][0], temp1[2][0], temp3[0][0], temp3[3][0], 'a'],
                                 'SAND', [temp3[3][0], temp1[2][0], temp3[0][0], temp3[3][0], 'a']]
                elif temp3[1][4] == 'v' and temp3[4][1][4] == 'pn':
                    # print('YES')
                    temp2 = [['x', temp1[2][0], 'x', temp3[4][0], 'v'], 'SAND',
                             [temp3[4][0], temp1[2][0], 'x', temp3[4][0], 'v']]
                    temp3.clear()
                    temp3.append(temp1[0])
                    temp3 += temp2
                    temp2.clear()
                    print('temp3', temp3)
                    if temp3[0][1][4] == 'pn' and temp3[1][4] == 'v':
                        temp2 = [[temp3[0][0], temp1[2][0], temp3[0][0], temp3[3][0], 'a'],
                                 'SAND', [temp3[3][0], temp1[2][0], temp3[0][0], temp3[3][0], 'a']]
                    elif temp3[0][1][4] == 'n' and temp3[1][4] == 'v':
                        temp2 = [[temp3[0][0], temp1[2][0], temp3[0][0], temp3[3][0], 'a'],
                                 'SAND', [temp3[3][0], temp1[2][0], temp3[0][0], temp3[3][0], 'a']]
        elif temp1[1][1][4] == 'v' and temp1[2][1][4] == 'n': #ฉันทาบ้านสีแดง
            temp2 = [['x', temp1[3][0], 'p', temp1[2][0], 'v']]
            temp3.append(temp1[0])
            temp3 += temp2
            temp2.clear()
            print('temp3', temp3)
            # print(temp1[0])
            # print(temp1[1])
            # print(temp1[2])
            # print(temp1[3])
            # print(temp3[0])
            # print(temp3[1])
            if temp3[0][1][4] == 'pn' and temp3[1][4] == 'v':
                # print("TEMP 1 :", temp1)
                temp2 = [[temp1[0][0], temp1[0][0], temp1[2][0], temp1[2][0], 'a'], ['SAND'],
                         [temp1[0][0], temp1[3][0], 'p', temp1[2][0], 'A32']]
            elif temp3[0][1][4] == 'n' and temp3[1][4] == 'v':
                temp2 = [[temp1[0][0], temp1[0][0], temp1[2][0], temp1[2][0], 'a'], ['SAND'],
                         [temp1[0][0], temp1[3][0], 'p', temp1[2][0], 'A32']]

    elif count_j == 4: #พิจารณาประโยค ฉันรับปากกาที่แม่ ตัวอย่างประโยค ฉันโยนปากกาที่โต๊ะ แม่โยนปากกาไปที่โต๊ะ
        if temp1[3][1][4] == 'pp' and temp1[4][1][4] == 'n':
            if temp1[3][1][4] == 'pp' and (temp1[3][0] == 'ใน' or 'ที่' or 'บน' or 'ใต้'):
                temp2 = [[temp1[3][0], temp1[3][0], temp1[4][0], 'x', 'v']]
                del temp1[3:5]
                temp1.append(temp2[0])
                temp2.clear()
                print("LMD : ", temp1)
                if temp1[2][1][4] == 'n' and (temp1[3][4] == 'v' and (temp1[3][0] == 'ใน' or 'ที่' or 'บน' or 'ใต้')):
                    temp2 = [[temp1[3][0], temp1[3][0], temp1[3][2], temp1[2][0], 'a']]
                    del temp1[2:5]
                    temp1.append(temp2[0])
                    temp2.clear()
                    print("TEMP1 :", temp1)
                    if temp1[1][0] == 'โยน' and (temp1[2][4] == 'a' and temp1[2][0] == 'ใน'):
                        temp2 = [['x', temp1[2][3], 'hand', 'hand', 'v'], 'SAND', ['x', 'hand', 'p', temp1[2][2], 'v'],
                                 'CAND', ['x', temp1[2][3], 'hand', 'air', 'v'], 'SAND', temp1[2]]
                        temp3 = temp1[0] + temp2
                        if temp3[1][4] == 'pn' and temp3[2][4] == 'v':
                            temp2 = [[temp3[0], temp1[2][3], 'hand', 'hand', 'a'], 'SAND',
                                     [temp3[0], 'hand', 'p', temp1[2][2], 'a'], 'CAND',
                                     [temp3[0], temp1[2][3], 'hand', 'air', 'a'], temp3[7], temp3[8]]
                        elif temp3[1][4] == 'n' and temp3[2][4] == 'v':
                            temp2 = [[temp3[0], temp1[2][3], 'hand', 'hand', 'a'], 'SAND',
                                     [temp3[0], 'hand', 'p', temp1[2][2], 'a'], 'CAND',
                                     [temp3[0], temp1[2][3], 'hand', 'air', 'a'], temp3[7], temp3[8]]
                    elif temp1[1][0] == 'โยน' and (temp1[2][4] == 'a' and temp1[2][0] == 'ที่'):
                        temp2 = [['x', temp1[2][3], 'hand', 'hand', 'v'], 'SAND', ['x', 'hand', 'p', temp1[2][2], 'v'],
                                 'CAND', ['x', temp1[2][3], 'hand', 'air', 'v'], 'SAND', temp1[2]]
                        temp3 = temp1[0] + temp2
                        if temp3[1][4] == 'pn' and temp3[2][4] == 'v':
                            temp2 = [[temp3[0], temp1[2][3], 'hand', 'hand', 'a'], 'SAND',
                                     [temp3[0], 'hand', 'p', temp1[2][2], 'a'], 'CAND',
                                     [temp3[0], temp1[2][3], 'hand', 'air', 'a'], temp3[7], temp3[8]]
                        elif temp3[1][4] == 'n' and temp3[2][4] == 'v':
                            temp2 = [[temp3[0], temp1[2][3], 'hand', 'hand', 'a'], 'SAND',
                                     [temp3[0], 'hand', 'p', temp1[2][2], 'a'], 'CAND',
                                     [temp3[0], temp1[2][3], 'hand', 'air', 'a'], temp3[7], temp3[8]]
                    elif temp1[1][0] == 'โยน' and (temp1[2][4] == 'a' and temp1[2][0] == 'บน'):
                        temp2 = [['x', temp1[2][3], 'hand', 'hand', 'v'], 'SAND', ['x', 'hand', 'p', temp1[2][2], 'v'],
                                 'CAND', ['x', temp1[2][3], 'hand', 'air', 'v'], 'SAND', temp1[2]]
                        temp3 = temp1[0] + temp2
                        if temp3[1][4] == 'pn' and temp3[2][4] == 'v':
                            temp2 = [[temp3[0], temp1[2][3], 'hand', 'hand', 'a'], 'SAND',
                                     [temp3[0], 'hand', 'p', temp1[2][2], 'a'], 'CAND',
                                     [temp3[0], temp1[2][3], 'hand', 'air', 'a'], temp3[7], temp3[8]]
                        elif temp3[1][4] == 'n' and temp3[2][4] == 'v':
                            temp2 = [[temp3[0], temp1[2][3], 'hand', 'hand', 'a'], 'SAND',
                                     [temp3[0], 'hand', 'p', temp1[2][2], 'a'], 'CAND',
                                     [temp3[0], temp1[2][3], 'hand', 'air', 'a'], temp3[7], temp3[8]]
                    elif temp1[1][0] == 'โยน' and (temp1[2][4] == 'a' and temp1[2][0] == 'ใต้'):
                        temp2 = [['x', temp1[2][3], 'hand', 'hand', 'v'], 'SAND', ['x', 'hand', 'p', temp1[2][2], 'v'],
                                 'CAND', ['x', temp1[2][3], 'hand', 'air', 'v'], 'SAND', temp1[2]]
                        temp3 = temp1[0] + temp2
                        if temp3[1][4] == 'pn' and temp3[2][4] == 'v':
                            temp2 = [[temp3[0], temp1[2][3], 'hand', 'hand', 'a'], 'SAND',
                                     [temp3[0], 'hand', 'p', temp1[2][2], 'a'], 'CAND',
                                     [temp3[0], temp1[2][3], 'hand', 'air', 'a'], temp3[7], temp3[8]]
                        elif temp3[1][4] == 'n' and temp3[2][4] == 'v':
                            temp2 = [[temp3[0], temp1[2][3], 'hand', 'hand', 'a'], 'SAND',
                                     [temp3[0], 'hand', 'p', temp1[2][2], 'a'], 'CAND',
                                     [temp3[0], temp1[2][3], 'hand', 'air', 'a'], temp3[7], temp3[8]]
                if temp1[1][0] == 'ทาสี' and temp1[2][4] == 'a':
                    temp2 = [['x', temp1[2][3], 'p', temp1[2][2], 'A32']]
                    temp3 = temp1[0]+temp2
                    temp2.clear()
                    if temp3[1][4] == 'pn' and temp3[2][4] == 'A32':
                        temp2 = [[temp3[0], temp3[0], temp3[2][3], temp3[2][3], 'a'], ['SAND'],
                                 [temp3[0], temp1[2][3], 'p', temp1[2][2], 'A32']]
                    elif temp3[1][4] == 'n' and temp3[2][4] == 'A32':
                        temp2 = [[temp3[0], temp3[0], temp3[2][3], temp3[2][3], 'a'], ['SAND'],
                                 [temp3[0], temp1[2][3], 'p', temp1[2][2], 'A32']]
                elif temp1[1][1][4] == 'v' and temp1[2][4] == 'a': #ฉันถือปากกาที่โต๊ะ [['ฉัน', 'ปากกา', 'โต๊ะ', 'ฉัน', 'a']]
                    temp2 = [['x', temp1[2][3], temp1[2][2], 'q', 'a']]
                    temp3 = temp1[0]+temp2
                    print(temp3)
                    temp2.clear()
                    if temp3[1][4] == 'pn' and temp3[2][4] == 'a':
                        temp2 = [[temp1[0][0], temp1[2][3], temp3[2][2], temp1[0][0], 'a']]
                    elif temp3[1][4] == 'n' and temp3[2][4] == 'a':
                        temp2 = [[temp1[0][0], temp1[2][3], temp3[2][2], temp1[0][0], 'a']]

    print('LMD temp2 : ', temp2)

    print('LMD temp2 : ', temp2)
    call_back(temp2)
    lmd_image(temp2)
    return temp2

def start(messegesinput):
    # sen = input("text: ")
    # screen.resetscreen()
    sen = messegesinput
    screen.clearscreen()
    t1.goto(200, -200)
    t2.goto(200, -200)
    t3.goto(200, -200)
    run(sen)


    # start()
def show_data_system():
    import webbrowser as wb
    wb.open(r'D:\Python for Project-2021\Python for Project\word_in_system.pdf')

def get_sentence(messegesinput):

    start(messegesinput)

def call_back(temp2):
    messageshow['text'] = temp2


# -----------------------------------------# รับประโยคนำเข้า
DataEntryFrame = Frame(App, bg='#99bbff', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=65, width=1300, height=130)
frontlabel = Label(DataEntryFrame, text='กรุณากรอกประโยค', width=30, font=('Angsana New', 24, 'italic bold'),
                   bg='#99bbff')
frontlabel.place(x=0, y=10)

Input_Sentence = Entry(DataEntryFrame, font=('Angsana New', 24, 'italic bold'), bg='white')
Input_Sentence.place(x=300, y=10, width=350, height=40)

# --------------------------------------------#button
enterbuttom = Button(DataEntryFrame, text='แปลประโยค', font=('Angsana New', 18, 'italic bold'), command=lambda: get_sentence(Input_Sentence.get()))
enterbuttom.place(x=700, y=10, width=100, height=40)
buttonword = Button(DataEntryFrame, text='ดูคำศัพท์ในระบบ', font=('Angsana New', 18, 'italic bold'), command=lambda:show_data_system())
buttonword.place(x=850, y=10, width=150, height=40)

# ------------------------------------------# แสดงประโยค LMD
frontlabel = Label(DataEntryFrame, text='ประโยคการแปลความโดยตรงจากจินภาพ', width=20, font=('Angsana New', 18, 'italic bold'), bg='#99bbff')
frontlabel.place(x=0, y=60, width=300, height=50)
messageshow = Label(DataEntryFrame, text="", font=('Angsana New', 20, 'italic bold'), bg='white')
messageshow.place(x=300, y=60, width=900, height=50)

# -------------------------------------------# แสดงข้อความในระบบ
# frontlabel = Label(DataEntryFrame, text='คำศัพท์ ในระบบ', width=20, font=('Angsana New', 24, 'italic bold'), bg='#99bbff')
# frontlabel.place(x=140, y=280)
# Label(DataEntryFrame, image=All_Vocab).place(x=10,y=340)

# -------------------------------------------# แสดงรูปภาพ
ShowDataFrame = Canvas(App, bg='white', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=10, y=200, width=1300, height=551)

SS = 'ยินดีต้อนรับสู่ระบบต้นแบบความเข้าใจภาษาไทยโดยใช้ทฤษฎีการแปลความหมายโดยตรงจากจินตภาพ'
SliderLabel = Label(App, text=SS, font=('Angsana New ', 14), relief=RIDGE, borderwidth=4, width=90, bg='cyan')
SliderLabel.place(x=150, y=0)



drw = Canvas(App, width=800, height=600)
drw.pack()

t1 = turtle.RawTurtle(ShowDataFrame)
t2 = turtle.RawTurtle(ShowDataFrame)
t3 = turtle.RawTurtle(ShowDataFrame)
screen = t1.getscreen()
t1.color("white")
t2.color("white")
t3.color("white")


def lmd_image(temp2):

    img = [['จาน', r"D:\Python for Project-2021\Python for Project\GIF\จาน.gif"],['ส้อม', r"D:\Python for Project-2021\Python for Project\GIF\ส้อม.gif"],
           ['ตู้', r"D:\Python for Project-2021\Python for Project\GIF\ตู้.gif"], ['แจกัน', r"D:\Python for Project-2021\Python for Project\GIF\แจกัน.gif"],
           ['แก้วน้ำ', r"D:\Python for Project-2021\Python for Project\GIF\แก้วน้ำ.gif"], ['แว่นตา', r"D:\Python for Project-2021\Python for Project\GIF\แว่นตา.gif"],
           ['แหวน', r"D:\Python for Project-2021\Python for Project\GIF\แหวน.gif"], ['ลูกโป่ง', r"D:\Python for Project-2021\Python for Project\GIF\ลูกโป่ง.gif"],
           ['ดินสอ', r"D:\Python for Project-2021\Python for Project\GIF\ดินสอ.gif"], ['รองเท้า', r"D:\Python for Project-2021\Python for Project\GIF\รองเท้า.gif"],
           ['ดอกไม้', r"D:\Python for Project-2021\Python for Project\GIF\ดอกไม้.gif"], ['ช้อน', r"D:\Python for Project-2021\Python for Project\GIF\ช้อน.gif"],
           ['นาฬิกา', r"D:\Python for Project-2021\Python for Project\GIF\นาฬิกา.gif"], ['หนังสือ', r"D:\Python for Project-2021\Python for Project\GIF\หนังสือ.gif"],
           ['ปืน', r"D:\Python for Project-2021\Python for Project\GIF\ปืน.gif"], ['ขวด', r"D:\Python for Project-2021\Python for Project\GIF\ขวด.gif"],
           ['ตะหลิว', r"D:\Python for Project-2021\Python for Project\GIF\ตะหลิว.gif"], ['กระทะ', r"D:\Python for Project-2021\Python for Project\GIF\กระทะ.gif"],
           ['หวี', r"D:\Python for Project-2021\Python for Project\GIF\หวี.gif"], ['ตู้เย็น', r"D:\Python for Project-2021\Python for Project\GIF\ตู้เย็น.gif"],
           ['เข็มขัด', r"D:\Python for Project-2021\Python for Project\GIF\เข็มขัด.gif"], ['สมุด', r"D:\Python for Project-2021\Python for Project\GIF\สมุด.gif"],
           ['พัดลม', r"D:\Python for Project-2021\Python for Project\GIF\พัดลม.gif"],  ['ลูกบอล', r"D:\Python for Project-2021\Python for Project\GIF\ลูกบอล.gif"],
           ['เตารีด', r"D:\Python for Project-2021\Python for Project\GIF\เตารีด.gif"], ['ไม้กวาด', r"D:\Python for Project-2021\Python for Project\GIF\ไม้กวาด.gif"],
           ['วิทยุ', r"D:\Python for Project-2021\Python for Project\GIF\วิทยุ.gif"], ['กล่อง', r"D:\Python for Project-2021\Python for Project\GIF\กล่อง.gif"],
           ['มีด', r"D:\Python for Project-2021\Python for Project\GIF\มีด.gif"], ['โรงเรียน', r"D:\Python for Project-2021\Python for Project\GIF\โรงเรียน.gif"],
           ['ปากกา', r"D:\Python for Project-2021\Python for Project\GIF\ปากกา.gif"], ['ฉัน', r"D:\Python for Project-2021\Python for Project\GIF\ฉัน3.gif"],
           ['โต๊ะ', r"D:\Python for Project-2021\Python for Project\GIF\โต๊ะ.gif"]]


    t1.penup()
    t2.penup()
    t3.penup()
    t1.shape("turtle")
    t2.shape("turtle")
    t3.shape("turtle")
    lmd_img = temp2
    print("ประโยคเพื่อการอธิบายจินตภาพ : ",lmd_img)
    for c in range(len(lmd_img)):
        count_c = c
        # print(lmd_img[c],c)
        if count_c >= 3:
            screen.clearscreen()
            popup_alert()
            break
        if lmd_img[0][4] == 'A32':
            popup_alert()
            break
        if (lmd_img[0][0] == lmd_img[0][2]) and (lmd_img[0][2] != lmd_img[0][3]):
            popup_alert()
            break
        for cc in range(len(lmd_img[0])):
            # print(img[cc])
            for p in range(len(img[0:50])):  # นับที่อยู่ของภาพ
                # print(p)
                if count_c == 0:
                    if (lmd_img[0][cc] == lmd_img[0][1]) and (lmd_img[0][4] != 'A32'):
                        if (lmd_img[0][0] == img[p][0]) and (lmd_img[0][0] != lmd_img[0][2]):
                            t1.goto(200, -210)
                            screen.addshape(img[p][1])
                            t1.shape(img[p][1])
                            print('1')
                        elif (lmd_img[0][0] == img[p][0]) and (lmd_img[0][2] == lmd_img[0][3]):
                            t1.goto(200, -210)
                            screen.addshape(img[p][1])
                            t1.shape(img[p][1])
                            print('1.1')
                        elif (lmd_img[0][0] == img[p][0]) and (lmd_img[0][0] == lmd_img[0][4]):
                            t1.goto(200, -210)
                            screen.addshape(img[p][1])
                            t1.shape(img[p][1])
                            print('1.2')
                        elif (lmd_img[0][2] != lmd_img[0][3]) and lmd_img[0][2] == 'p':  # ไปที่ใด
                            if lmd_img[0][3] == img[p][0]:
                                t2.goto(800, -100)
                                screen.addshape(img[p][1])
                                t2.shape(img[p][1])
                                print('2')
                        elif (lmd_img[0][2] != lmd_img[0][3]) and lmd_img[0][3] == 'p':  # มาที่ใด
                            if lmd_img[0][2] == img[p][0]:
                                t2.goto(50, -100)
                                screen.addshape(img[p][1])
                                t2.shape(img[p][1])
                                print('3')
                    elif lmd_img[0][4] == 'A32':
                        popup_alert()
                        break
                    elif (lmd_img[0][cc] != lmd_img[0][1]) and (lmd_img[0][0] != lmd_img[0][1]):  # หยิบ จับ ถือ อยู่
                        if lmd_img[0][1] == img[p][0]:
                            t2.goto(390, -130)
                            screen.addshape(img[p][1])
                            t2.shape(img[p][1])
                            print('4')
                        elif (lmd_img[0][2] != lmd_img[0][3]) and (lmd_img[0][0] != lmd_img[0][2]):  # ถือที่ตำแหน่งใด
                            if lmd_img[0][2] == img[p][0]:
                                t3.goto(400, -200)
                                screen.addshape(img[p][1])
                                t3.shape(img[p][1])
                                print('5')
                    elif (lmd_img[0][cc] == lmd_img[0][3]) and (lmd_img[0][2] == lmd_img[0][3]):
                        if lmd_img[0][3] == img[p][0]:
                            t2.goto(30, 90)
                            screen.addshape(img[p][1])
                            t2.shape(img[p][1])
                            print('6')
                if count_c == 2:
                    if lmd_img[2][0] == 'บน':
                        if lmd_img[0][cc] == lmd_img[0][1]:
                            if lmd_img[0][0] == img[p][0]:
                                t2.goto(400, -150)
                                screen.addshape(img[p][1])
                                t2.shape(img[p][1])
                                print("7")
                        elif lmd_img[0][cc] == lmd_img[0][3]:
                            if lmd_img[0][2] == img[p][0]:
                                t1.goto(400, -230)
                                screen.addshape(img[p][1])
                                t1.shape(img[p][1])
                                print("8")
                    if lmd_img[2][0] == 'ใน':
                        if lmd_img[0][cc] == lmd_img[0][1]:
                            if lmd_img[0][0] == img[p][0]:
                                t2.goto(450, -270)
                                screen.addshape(img[p][1])
                                t2.shape(img[p][1])
                        elif lmd_img[0][cc] == lmd_img[0][3]:
                            if lmd_img[0][2] == img[p][0]:
                                t1.goto(450, -250)
                                screen.addshape(img[p][1])
                                t1.shape(img[p][1])
                    if lmd_img[2][0] == 'ใต้':
                        if lmd_img[0][cc] == lmd_img[0][1]:
                            if lmd_img[0][0] == img[p][0]:
                                t2.goto(450, -300)
                                screen.addshape(img[p][1])
                                t2.shape(img[p][1])
                        elif lmd_img[0][cc] == lmd_img[0][3]:
                            if lmd_img[0][2] == img[p][0]:
                                t1.goto(450, -100)
                                screen.addshape(img[p][1])
                                t1.shape(img[p][1])
                    if lmd_img[2][0] == 'ที่':
                        if lmd_img[0][cc] == lmd_img[0][1]:
                            if lmd_img[0][0] == img[p][0]:
                                t2.goto(450, -270)
                                screen.addshape(img[p][1])
                                t2.shape(img[p][1])
                        elif lmd_img[0][cc] == lmd_img[0][3]:
                            if lmd_img[0][2] == img[p][0]:
                                t1.goto(450, -250)
                                screen.addshape(img[p][1])
                                t1.shape(img[p][1])
                # if count_c > 2:
                #     popup_alert()
                #     continue


mainloop()


