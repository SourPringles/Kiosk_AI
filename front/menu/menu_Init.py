from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import front
import back1

import time #for Test

#형식: 메뉴이름, 가격, 이미지경로, 분류
##menudata[3]

def menuWidget_Load(self, type) :
        start = time.time()#

        self.menuList.clear()
        menuDB = []
        if 'menuDB_origin' not in locals()  :
            menuDB_origin = back1.get_menu_price_path_category()    #List
        if 'optionDB' not in locals() :
            optionDB = back1.get_menu_option()                      #Dict

        if type == 'ALL' or type == '' :
            menuDB = menuDB_origin
        else :
            for item in menuDB_origin :
                if item[3] == '커피(ICE)' or item[3] =='커피(HOT)' :
                    menuType = '커피'
                else :
                    menuType = item[3]

                if menuType == type :
                    menuDB.append(item)
                else :
                    pass

        ## menuDB = [menuType: menuList[]]
        start2 = time.time()
        for list in menuDB :
            list.append(optionDB[list[0]][1])
        end2 = time.time()
        print(f'실행 시간: {end2 - start2}')#

    
        menuData = []

        for i in range(0, len(menuDB), 4) :
            menuData.append(menuDB[i:i + 4])

        for itemSet in menuData :
            item_Widget = front.menu_ItemSet(self.menuList, itemSet, self)
            item = QListWidgetItem()
            item.setSizeHint(item_Widget.sizeHint())

            self.menuList.addItem(item)
            self.menuList.setItemWidget(item, item_Widget)

        end = time.time()#
        print(f'메뉴 로딩 시간: {end - start}')#
