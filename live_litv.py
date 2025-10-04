# -*- coding: utf-8 -*-
# @Author  : Doubebly
# @Time    : 2025/3/23 21:55
import base64
import sys
import time
import json
import requests
sys.path.append('..')
from base.spider import Spider


class Spider(Spider):
    def getName(self):
        return "Litv"

    def init(self, extend):
        self.extend = extend
        try:
            self.extendDict = json.loads(extend)
        except:
            self.extendDict = {}

        proxy = self.extendDict.get('proxy', None)
        if proxy is None:
            self.is_proxy = False
        else:
            self.proxy = proxy
            self.is_proxy = True
        pass

    def getDependence(self):
        return []

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass


    def liveContent(self, url):



        a = ['#EXTM3U', '#EXTINF:-1 tvg-id="����" tvg-name="����" tvg-logo="https://logo.doube.eu.org/����.png" group-title="",����', f'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv002,1,10', '#EXTINF:-1 tvg-id="����̨��̨" tvg-name="����̨��̨" tvg-logo="https://logo.doube.eu.org/����̨��̨.png" group-title="",����̨��̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv001,1,6', '#EXTINF:-1 tvg-id="����̨��̨" tvg-name="����̨��̨" tvg-logo="https://logo.doube.eu.org/����̨��̨.png" group-title="",����̨��̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv156,1,6', '#EXTINF:-1 tvg-id="���ӵ�һ̨" tvg-name="���ӵ�һ̨" tvg-logo="https://logo.doube.eu.org/���ӵ�һ̨.png" group-title="",���ӵ�һ̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv003,1,6', '#EXTINF:-1 tvg-id="��������̨" tvg-name="��������̨" tvg-logo="https://logo.doube.eu.org/��������̨.png" group-title="",��������̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv13,1,7', '#EXTINF:-1 tvg-id="��������̨" tvg-name="��������̨" tvg-logo="https://logo.doube.eu.org/��������̨.png" group-title="",��������', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv07,1,7', '#EXTINF:-1 tvg-id="����Ӱ��̨" tvg-name="����Ӱ��̨" tvg-logo="https://logo.doube.eu.org/����Ӱ��̨.png" group-title="",����Ӱ��', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv09,1,2', '#EXTINF:-1 tvg-id="����Ӱ��̨" tvg-name="����Ӱ��̨" tvg-logo="https://logo.doube.eu.org/����Ӱ��̨.png" group-title="",����Ӱ��', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv09,1,7', '#EXTINF:-1 tvg-id="��������̨" tvg-name="��������̨" tvg-logo="https://logo.doube.eu.org/��������̨.png" group-title="",��������', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv004,1,8', '#EXTINF:-1 tvg-id="̨��Ϸ��̨" tvg-name="̨��Ϸ��̨" tvg-logo="https://logo.doube.eu.org/̨��Ϸ��̨.png" group-title="",̨��Ϸ��̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn22,5,2', '#EXTINF:-1 tvg-id="��������̨" tvg-name="��������̨" tvg-logo="https://logo.doube.eu.org/��������̨.png" group-title="",��������', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn21,5,2', '#EXTINF:-1 tvg-id="����Ϸ��̨" tvg-name="����Ϸ��̨" tvg-logo="https://logo.doube.eu.org/����Ϸ��̨.png" group-title="",����Ϸ��', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn18,5,6', '#EXTINF:-1 tvg-id="������Ӱ̨" tvg-name="������Ӱ̨" tvg-logo="https://logo.doube.eu.org/������Ӱ̨.png" group-title="",������Ӱ', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn03,5,6', '#EXTINF:-1 tvg-id="�����պ�̨" tvg-name="�����պ�̨" tvg-logo="https://logo.doube.eu.org/�����պ�̨.png" group-title="",�����պ�', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn11,5,2', '#EXTINF:-1 tvg-id="����ż��̨" tvg-name="����ż��̨" tvg-logo="https://logo.doube.eu.org/����ż��̨.png" group-title="",����ż��', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn12,5,2', '#EXTINF:-1 tvg-id="������Ƭ̨" tvg-name="������Ƭ̨" tvg-logo="https://logo.doube.eu.org/������Ƭ̨.png" group-title="",������Ƭ', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn02,5,2', '#EXTINF:-1 tvg-id="������̨ͨ" tvg-name="������̨ͨ" tvg-logo="https://logo.doube.eu.org/������̨ͨ.png" group-title="",������ͨ', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn01,4,2', '#EXTINF:-1 tvg-id="������̨ͨ" tvg-name="������̨ͨ" tvg-logo="https://logo.doube.eu.org/������̨ͨ.png" group-title="",������ͨ', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn01,4,5', '#EXTINF:-1 tvg-id="�����ۺ�̨" tvg-name="�����ۺ�̨" tvg-logo="https://logo.doube.eu.org/�����ۺ�̨.png" group-title="",�����ۺ�̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv046,1,8', '#EXTINF:-1 tvg-id="�����ձ�̨" tvg-name="�����ձ�̨" tvg-logo="https://logo.doube.eu.org/�����ձ�̨.png" group-title="",�����ձ�̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv047,1,8', '#EXTINF:-1 tvg-id="���컶��̨" tvg-name="���컶��̨" tvg-logo="https://logo.doube.eu.org/���컶��̨.png" group-title="",���컶��̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv054,1,8', '#EXTINF:-1 tvg-id="����ӳ��" tvg-name="����ӳ��" tvg-logo="https://logo.doube.eu.org/����ӳ��.png" group-title="",����ӳ��', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv055,1,8', '#EXTINF:-1 tvg-id="�����Ӱ̨" tvg-name="�����Ӱ̨" tvg-logo="https://logo.doube.eu.org/�����Ӱ̨.png" group-title="",�����Ӱ̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv061,1,7', '#EXTINF:-1 tvg-id="��������̨" tvg-name="��������̨" tvg-logo="https://logo.doube.eu.org/��������̨.png" group-title="",��������̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv062,1,8', '#EXTINF:-1 tvg-id="�������̨" tvg-name="�������̨" tvg-logo="https://logo.doube.eu.org/�������̨.png" group-title="",�������̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv063,1,6', '#EXTINF:-1 tvg-id="����Ϸ��̨" tvg-name="����Ϸ��̨" tvg-logo="https://logo.doube.eu.org/����Ϸ��̨.png" group-title="",����Ϸ��̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv058,1,8', '#EXTINF:-1 tvg-id="������Ѷ̨" tvg-name="������Ѷ̨" tvg-logo="https://logo.doube.eu.org/������Ѷ̨.png" group-title="",������Ѷ̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv065,1,8', '#EXTINF:-1 tvg-id="���쿨̨ͨ" tvg-name="���쿨̨ͨ" tvg-logo="https://logo.doube.eu.org/���쿨̨ͨ.png" group-title="",���쿨̨ͨ', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv044,1,8', '#EXTINF:-1 tvg-id="TVBS" tvg-name="TVBS" tvg-logo="https://logo.doube.eu.org/TVBS.png" group-title="",Tvbs', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv073,1,2', '#EXTINF:-1 tvg-id="TVBS����" tvg-name="TVBS����" tvg-logo="https://logo.doube.eu.org/TVBS����.png" group-title="",Tvbs����̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv072,1,2', '#EXTINF:-1 tvg-id="TVBS����̨" tvg-name="TVBS����̨" tvg-logo="https://logo.doube.eu.org/TVBS����̨.png" group-title="",Tvbs����̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv067,1,8', '#EXTINF:-1 tvg-id="TVBS����̨" tvg-name="TVBS����̨" tvg-logo="https://logo.doube.eu.org/TVBS����̨.png" group-title="",Tvbs����̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv068,1,7', '#EXTINF:-1 tvg-id="̨��" tvg-name="̨��" tvg-logo="https://logo.doube.eu.org/̨��.png" group-title="",̨��', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv066,1,2', '#EXTINF:-1 tvg-id="̨��" tvg-name="̨��" tvg-logo="https://logo.doube.eu.org/̨��.png" group-title="",̨��', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv066,1,6', '#EXTINF:-1 tvg-id="̨�Ӳƾ�̨" tvg-name="̨�Ӳƾ�̨" tvg-logo="https://logo.doube.eu.org/̨�Ӳƾ�̨.png" group-title="",̨�Ӳƾ�', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv056,1,2', '#EXTINF:-1 tvg-id="̨������̨" tvg-name="̨������̨" tvg-logo="https://logo.doube.eu.org/̨������̨.png" group-title="",̨������', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv051,1,2', '#EXTINF:-1 tvg-id="̨������̨" tvg-name="̨������̨" tvg-logo="https://logo.doube.eu.org/̨������̨.png" group-title="",̨������', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv051,1,6', '#EXTINF:-1 tvg-id="��˹����" tvg-name="��˹����" tvg-logo="https://logo.doube.eu.org/��˹����.png" group-title="",��˹����', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn04,5,2', '#EXTINF:-1 tvg-id="��˹����1" tvg-name="��˹����1" tvg-logo="https://logo.doube.eu.org/��˹����1.png" group-title="",��˹����1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn05,5,2', '#EXTINF:-1 tvg-id="��˹����2" tvg-name="��˹����2" tvg-logo="https://logo.doube.eu.org/��˹����2.png" group-title="",��˹����2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn06,5,2', '#EXTINF:-1 tvg-id="��˹�˶�1" tvg-name="��˹�˶�1" tvg-logo="https://logo.doube.eu.org/��˹�˶�1.png" group-title="",��˹�˶�1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn07,5,2', '#EXTINF:-1 tvg-id="��˹�˶�2" tvg-name="��˹�˶�2" tvg-logo="https://logo.doube.eu.org/��˹�˶�2.png" group-title="",��˹�˶�2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn08,5,2', '#EXTINF:-1 tvg-id="��˹����1" tvg-name="��˹����1" tvg-logo="https://logo.doube.eu.org/��˹����1.png" group-title="",��˹����', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn09,5,2', '#EXTINF:-1 tvg-id="��˹����1" tvg-name="��˹����1" tvg-logo="https://logo.doube.eu.org/��˹����1.png" group-title="",��˹����', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn10,5,2', '#EXTINF:-1 tvg-id="��˹����2" tvg-name="��˹����2" tvg-logo="https://logo.doube.eu.org/��˹����2.png" group-title="",��˹����2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn13,4,2', '#EXTINF:-1 tvg-id="����" tvg-name="����" tvg-logo="https://logo.doube.eu.org/����.png" group-title="",����', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv040,1,6', '#EXTINF:-1 tvg-id="����ݼ��̨" tvg-name="����ݼ��̨" tvg-logo="https://logo.doube.eu.org/����ݼ��̨.png" group-title="",����ݼ��', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv064,1,8', '#EXTINF:-1 tvg-id="��������̨" tvg-name="��������̨" tvg-logo="https://logo.doube.eu.org/��������̨.png" group-title="",��������', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv074,1,2', '#EXTINF:-1 tvg-id="���Ӿ���̨" tvg-name="���Ӿ���̨" tvg-logo="https://logo.doube.eu.org/���Ӿ���̨.png" group-title="",���Ӿ���', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv080,1,6', '#EXTINF:-1 tvg-id="�����������" tvg-name="�����������" tvg-logo="https://logo.doube.eu.org/�����������.png" group-title="",�����������', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv006,1,9', '#EXTINF:-1 tvg-id="��������" tvg-name="��������" tvg-logo="https://logo.doube.eu.org/��������.png" group-title="",��������', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv009,2,7', '#EXTINF:-1 tvg-id="��������" tvg-name="��������" tvg-logo="https://logo.doube.eu.org/��������.png" group-title="",��������̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv109,1,7', '#EXTINF:-1 tvg-id="�Ƿ�����" tvg-name="�Ƿ�����" tvg-logo="https://logo.doube.eu.org/�Ƿ�����.png" group-title="",�Ƿ�����', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv010,1,6', '#EXTINF:-1 tvg-id="�Ƿ���ҵ" tvg-name="�Ƿ���ҵ" tvg-logo="https://logo.doube.eu.org/�Ƿ���ҵ.png" group-title="",�Ƿ���ҵ', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv048,1,2', '#EXTINF:-1 tvg-id="�������̨" tvg-name="�������̨" tvg-logo="https://logo.doube.eu.org/�������̨.png" group-title="",�������̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn14,1,2', '#EXTINF:-1 tvg-id="�������̨��̨" tvg-name="�������̨��̨" tvg-logo="https://logo.doube.eu.org/�������̨��̨.png" group-title="",�������̨��̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv156,1,6', '#EXTINF:-1 tvg-id="�˴󾫲�" tvg-name="�˴󾫲�" tvg-logo="https://logo.doube.eu.org/�˴󾫲�.png" group-title="",�˴󾫲�̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv034,1,6', '#EXTINF:-1 tvg-id="�˴�����" tvg-name="�˴�����" tvg-logo="https://logo.doube.eu.org/�˴�����.png" group-title="",�˴�����̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv039,1,7', '#EXTINF:-1 tvg-id="����Ƶ��1" tvg-name="����Ƶ��1" tvg-logo="https://logo.doube.eu.org/����Ƶ��1.png" group-title="",����Ƶ��1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv084,1,6', '#EXTINF:-1 tvg-id="����Ƶ��2" tvg-name="����Ƶ��2" tvg-logo="https://logo.doube.eu.org/����Ƶ��2.png" group-title="",����Ƶ��2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv085,1,5', '#EXTINF:-1 tvg-id="����Ϣ1" tvg-name="����Ϣ1" tvg-logo="https://logo.doube.eu.org/����Ϣ1.png" group-title="",����Ϣ1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv16,1,2', '#EXTINF:-1 tvg-id="����Ϣ1" tvg-name="����Ϣ1" tvg-logo="https://logo.doube.eu.org/����Ϣ1.png" group-title="",����Ϣ1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv16,1,6', '#EXTINF:-1 tvg-id="����Ϣ2" tvg-name="����Ϣ2" tvg-logo="https://logo.doube.eu.org/����Ϣ2.png" group-title="",����Ϣ2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv17,1,2', '#EXTINF:-1 tvg-id="����Ϣ2" tvg-name="����Ϣ2" tvg-logo="https://logo.doube.eu.org/����Ϣ2.png" group-title="",����Ϣ2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv17,1,6', '#EXTINF:-1 tvg-id="����Ϸ��̨" tvg-name="����Ϸ��̨" tvg-logo="https://logo.doube.eu.org/����Ϸ��̨.png" group-title="",����Ϸ��̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv045,1,6', '#EXTINF:-1 tvg-id="����̨ͨ" tvg-name="����̨ͨ" tvg-logo="https://logo.doube.eu.org/����̨ͨ.png" group-title="",����̨ͨ', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv057,1,8', '#EXTINF:-1 tvg-id="��ɭ����̨" tvg-name="��ɭ����̨" tvg-logo="https://logo.doube.eu.org/��ɭ����̨.png" group-title="",��ɭ����', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv152,1,6', '#EXTINF:-1 tvg-id="��ɭ�ƾ�����̨" tvg-name="��ɭ�ƾ�����̨" tvg-logo="https://logo.doube.eu.org/��ɭ�ƾ�����̨.png" group-title="",��ɭ�ƾ�����', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv153,1,2', '#EXTINF:-1 tvg-id="��ɭ�ƾ�����̨" tvg-name="��ɭ�ƾ�����̨" tvg-logo="https://logo.doube.eu.org/��ɭ�ƾ�����̨.png" group-title="",��ɭ�ƾ�����', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv153,1,6', '#EXTINF:-1 tvg-id="Ӱ�Ԕ�λ�Ӱ̨" tvg-name="Ӱ�Ԕ�λ�Ӱ̨" tvg-logo="https://logo.doube.eu.org/Ӱ�Ԕ�λ�Ӱ̨.png" group-title="",Ӱ�Ԕ�λ�Ӱ̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv011,1,6', '#EXTINF:-1 tvg-id="���ɻ��ʼ�ʵ" tvg-name="���ɻ��ʼ�ʵ" tvg-logo="https://logo.doube.eu.org/���ɻ��ʼ�ʵ.png" group-title="",ҕ�{�A�ʼo���l��', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv013,1,6', '#EXTINF:-1 tvg-id="ʱ���˶�X" tvg-name="ʱ���˶�X" tvg-logo="https://logo.doube.eu.org/ʱ���˶�X.png" group-title="",ʱ���˶�X', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv014,1,5', '#EXTINF:-1 tvg-id="Globetrotter" tvg-name="Globetrotter" tvg-logo="https://logo.doube.eu.org/Globetrotter.png" group-title="",GLOBETROTTER', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv016,1,6', '#EXTINF:-1 tvg-id="amc��Ӱ̨" tvg-name="amc��Ӱ̨" tvg-logo="https://logo.doube.eu.org/amc��Ӱ̨.png" group-title="",amc��Ӱ̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv017,1,6', '#EXTINF:-1 tvg-id="������Ƶ��" tvg-name="������Ƶ��" tvg-logo="https://logo.doube.eu.org/������Ƶ��.png" group-title="",������Ƶ��', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv018,1,6', '#EXTINF:-1 tvg-id="����" tvg-name="����" tvg-logo="https://logo.doube.eu.org/����.png" group-title="",����', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv041,1,6', '#EXTINF:-1 tvg-id="����Ϸ��" tvg-name="����Ϸ��" tvg-logo="https://logo.doube.eu.org/����Ϸ��.png" group-title="",����Ϸ��', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv042,1,6', '#EXTINF:-1 tvg-id="�ͼҵ���̨" tvg-name="�ͼҵ���̨" tvg-logo="https://logo.doube.eu.org/�ͼҵ���̨.png" group-title="",�ͼҵ���̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv043,1,6', '#EXTINF:-1 tvg-id="�ɲ�Ӱ��̨" tvg-name="�ɲ�Ӱ��̨" tvg-logo="https://logo.doube.eu.org/�ɲ�Ӱ��̨.png" group-title="",�ɲ�Ӱ��', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv049,1,8', '#EXTINF:-1 tvg-id="��������" tvg-name="��������" tvg-logo="https://logo.doube.eu.org/��������.png" group-title="",��������', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv052,1,2', '#EXTINF:-1 tvg-id="GINXEsportsTV" tvg-name="GINXEsportsTV" tvg-logo="https://logo.doube.eu.org/GINXEsportsTV.png" group-title="",GinxTV', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv053,1,8', '#EXTINF:-1 tvg-id="CLASSICA�ŵ���" tvg-name="CLASSICA�ŵ���" tvg-logo="https://logo.doube.eu.org/CLASSICA�ŵ���.png" group-title="",�ŵ�����̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv059,1,6', '#EXTINF:-1 tvg-id="ELTV����" tvg-name="ELTV����" tvg-logo="https://logo.doube.eu.org/ELTV����.png" group-title="",����������', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv070,1,7', '#EXTINF:-1 tvg-id="����������̨" tvg-name="����������̨" tvg-logo="https://logo.doube.eu.org/����������̨.png" group-title="",������', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv075,1,2', '#EXTINF:-1 tvg-id="��������̨" tvg-name="��������̨" tvg-logo="https://logo.doube.eu.org/��������̨.png" group-title="",��������̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv076,1,2', '#EXTINF:-1 tvg-id="TraceSportStars" tvg-name="TraceSportStars" tvg-logo="https://logo.doube.eu.org/TraceSportStars.png" group-title="",TRACE SPORTS STARS', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv082,1,2', '#EXTINF:-1 tvg-id="ARIRANG" tvg-name="ARIRANG" tvg-logo="https://logo.doube.eu.org/ARIRANG.png" group-title="",������', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv079,1,2', '#EXTINF:-1 tvg-id="TraceUrban" tvg-name="TraceUrban" tvg-logo="https://logo.doube.eu.org/TraceUrban.png" group-title="",TRACE URBAN', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv082,1,6', '#EXTINF:-1 tvg-id="MezzoLiveHD" tvg-name="MezzoLiveHD" tvg-logo="https://logo.doube.eu.org/MezzoLiveHD.png" group-title="",MEZZO LIVE', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv083,1,6', '#EXTINF:-1 tvg-id="��������̨" tvg-name="��������̨" tvg-logo="https://logo.doube.eu.org/��������̨.png" group-title="",��������̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv101,1,5', '#EXTINF:-1 tvg-id="��������̨" tvg-name="��������̨" tvg-logo="https://logo.doube.eu.org/��������̨.png" group-title="",��������̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv101,1,6', '#EXTINF:-1 tvg-id="��1��ҵ̨" tvg-name="��1��ҵ̨" tvg-logo="https://logo.doube.eu.org/��1��ҵ̨.png" group-title="",��1��ҵ̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv104,1,7', '#EXTINF:-1 tvg-id="����֮��" tvg-name="����֮��" tvg-logo="https://logo.doube.eu.org/����֮��.png" group-title="",����֮��', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv03,1,7', '#EXTINF:-1 tvg-id="�뵺��������" tvg-name="�뵺��������" tvg-logo="https://logo.doube.eu.org/�뵺��������.png" group-title="",�뵺����', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv10,1,7', '#EXTINF:-1 tvg-id="Smart֪ʶ̨" tvg-name="Smart֪ʶ̨" tvg-logo="https://logo.doube.eu.org/Smart֪ʶ̨.png" group-title="",Smart֪ʶ̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn19,5,2', '#EXTINF:-1 tvg-id="ELTV����Ӣ��̨" tvg-name="ELTV����Ӣ��̨" tvg-logo="https://logo.doube.eu.org/ELTV����Ӣ��̨.png" group-title="",����Ӣ��̨', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn20,5,6']

        return '\n'.join(a)

    def homeContent(self, filter):
        return {}

    def homeVideoContent(self):
        return {}

    def categoryContent(self, cid, page, filter, ext):
        return {}

    def detailContent(self, did):
        return {}

    def searchContent(self, key, quick, page='1'):
        return {}

    def searchContentPage(self, keywords, quick, page):
        return {}

    def playerContent(self, flag, pid, vipFlags):
        return {}

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        if params['type'] == "ts":
            return self.get_ts(params)
        return [302, "text/plain", None, {'Location': 'https://sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-720p.mp4'}]
    def proxyM3u8(self, params):
        pid = params['pid']
        info = pid.split(',')
        a = info[0]
        b = info[1]
        c = info[2]
        timestamp = int(time.time() / 4 - 355017625)
        t = timestamp * 4
        m3u8_text = f'#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-TARGETDURATION:4\n#EXT-X-MEDIA-SEQUENCE:{timestamp}\n'
        for i in range(10):
            url = f'https://ntd-tgc.cdn.hinet.net/live/pool/{a}/litv-pc/{a}-avc1_6000000={b}-mp4a_134000_zho={c}-begin={t}0000000-dur=40000000-seq={timestamp}.ts'
            if self.is_proxy:
                url = f'http://127.0.0.1:9978/proxy?do=py&type=ts&url={self.b64encode(url)}'

            m3u8_text += f'#EXTINF:4,\n{url}\n'
            timestamp += 1
            t += 4
        return [200, "application/vnd.apple.mpegurl", m3u8_text]

    def get_ts(self, params):
        url = self.b64decode(params['url'])
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, stream=True, proxies=self.proxy)
        return [206, "application/octet-stream", response.content]

    def destroy(self):
        return '����Destroy'

    def b64encode(self, data):
        return base64.b64encode(data.encode('utf-8')).decode('utf-8')

    def b64decode(self, data):
        return base64.b64decode(data.encode('utf-8')).decode('utf-8')


if __name__ == '__main__':
    pass