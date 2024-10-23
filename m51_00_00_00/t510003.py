# -*- coding: utf-8 -*-
def t510003_1():
    """State 0,1"""
    t510003_x4()
    Quit()

def t510003_x0():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t510003_x1(gesture1=17, z1=9019, flag3=6067):
    """State 0,1"""
    if GetEventStatus(flag3) == 1:
        """State 2"""
        pass
    else:
        """State 3,4"""
        AcquireGesture(gesture1)
        OpenItemAcquisitionMenu(3, z1, 1)
        SetEventState(flag3, 1)
        assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t510003_x2(actionbutton1=_, flag1=6001, flag2=6000):
    """State 0"""
    while True:
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
                and not IsPlayerDead() and not IsCharacterDisabled())
        """State 2"""
        assert CompareBonfireState(1)
        """State 4"""
        assert GetEventStatus(flag1) == 1 and not GetEventStatus(flag2)
        """State 3"""
        if CompareBonfireState(0):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
        elif (not (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
              and not IsPlayerDead() and not IsCharacterDisabled())):
            pass
        elif not GetEventStatus(flag1) or GetEventStatus(flag2) == 1:
            pass
    """State 5"""
    return 0

def t510003_x3(action1=10010713):
    """State 0,1"""
    # action:10010713:"Game installation incomplete.\nCannot travel between bonfires."
    OpenGenericDialog(1, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t510003_x4():
    """State 0"""
    while True:
        """State 1"""
        call = t510003_x5()
        assert IsMultiplayerInProgress() == 1
        """State 2"""
        call = t510003_x8()
        assert not IsMultiplayerInProgress()
    """Unused"""
    """State 3"""
    return 0

def t510003_x5():
    """State 0,1"""
    if CompareBonfireLevel(5, 0) == 1:
        """State 2"""
        Label('L0')
    else:
        """State 3,15"""
        call = t510003_x2(actionbutton1=6100, flag1=6001, flag2=6000)
        if call.Done():
            """State 7"""
            TurnCharacterToFaceEntity(-1, 10000, -1)
            assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
            """State 4"""
            OfferHumanity()
            assert CompareBonfireLevel(5, 0) == 1
            """State 11"""
            RequestUnlockTrophy(41)
            """State 9"""
            UpdatePlayerRespawnPoint()
            Goto('L0')
        elif CompareBonfireLevel(5, 0) == 1:
            pass
    """State 14"""
    assert t510003_x2(actionbutton1=6101, flag1=6001, flag2=6000)
    """State 5"""
    ClearPlayerDamageInfo()
    """State 6"""
    SetTalkTime(1)
    """State 8"""
    TurnCharacterToFaceEntity(-1, 10000, -1)
    assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
    """State 10"""
    UpdatePlayerRespawnPoint()
    """State 12"""
    StartBonfireAnimLoop()
    call = t510003_x9()
    def ExitPause():
        EndBonfireKindleAnimLoop()
    if call.Done():
        Goto('L0')
    elif HasPlayerBeenAttacked() == 1 or GetDistanceToPlayer() > 3 or CompareBonfireState(0):
        """State 13"""
        assert t510003_x10()
        Goto('L0')
    """Unused"""
    """State 16"""
    return 0

def t510003_x6():
    """State 0,6"""
    call = t510003_x0()
    if call.Done() and CompareBonfireLevel(5, 0) == 1:
        pass
    elif call.Done():
        """State 2,7"""
        call = t510003_x2(actionbutton1=6100, flag1=6001, flag2=6000)
        if call.Done():
            """State 4"""
            TurnCharacterToFaceEntity(-1, 10000, -1)
            assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
            """State 3"""
            OfferHumanity()
            """State 5"""
            UpdatePlayerRespawnPoint()
            assert CompareBonfireLevel(5, 0) == 1
        elif CompareBonfireLevel(5, 0) == 1:
            pass
    """State 1"""
    Quit()
    """Unused"""
    """State 8"""
    return 0

def t510003_x7():
    """State 0,1"""
    assert t510003_x0()
    """State 2"""
    return 0

def t510003_x8():
    """State 0"""
    while True:
        """State 1"""
        call = t510003_x6()
        assert IsClientPlayer() == 1
        """State 2"""
        call = t510003_x7()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t510003_x9():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 2
    """State 21"""
    assert t510003_x1(gesture1=17, z1=9019, flag3=6067)
    """State 17"""
    MainBonfireMenuFlag()
    while True:
        """State 1"""
        ClearTalkListData()
        """State 2"""
        # action:15000150:"Travel"
        AddTalkListDataIf(GetEventStatus(14000101) == 1 or GetEventStatus(2050) == 1, 1, 15000150, -1)
        # action:15000130:"Attune Spell"
        AddTalkListDataIf(GetEventStatus(14000101) == 1 or GetEventStatus(2050) == 1, 2, 15000130, -1)
        # action:15000220:"Organize Storage Box"
        AddTalkListDataIf(GetEventStatus(14000101) == 1 or GetEventStatus(2050) == 1, 3, 15000220, -1)
        # action:15000005:"Leave"
        AddTalkListData(98, 80000001, -1)
        AddTalkListData(99, 15000005, -1)
        """State 4"""
        ShowShopMessage(1)
        if GetTalkListEntryResult() == 1:
            """State 3"""
            if GetEventStatus(2030) == 1:
                """State 18,8"""
                StartWarpMenuInit(-1)
                assert GetCurrentStateElapsedFrames() > 1
                """State 12"""
                if WasWarpMenuDestinationSelected() == 1:
                    break
                elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
                    """State 13"""
                    pass
            else:
                """State 16,20"""
                # action:10010713:"Game installation incomplete.\nCannot travel between bonfires."
                assert t510003_x3(action1=10010713)
        elif GetTalkListEntryResult() == 2:
            """State 6,7"""
            OpenMagicEquip(1000, 1000)
            assert not (CheckSpecificPersonMenuIsOpen(11, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 14,15"""
            OpenRepository()
            assert not (CheckSpecificPersonMenuIsOpen(3, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 98:
            assert t510003_x9999()
        elif (GetTalkListEntryResult() == 99 or not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not
              CheckSpecificPersonGenericDialogIsOpen(0))):
            """State 5,22"""
            return 0
    """State 11,19"""
    SetEventState(74000013, 1)
    """State 9"""
    Quit()

def t510003_x10():
    """State 0,1"""
    assert t510003_x0()
    """State 2"""
    return 0

def t510003_x9002(action3=13010000):
    """State 0,1"""
    OpenGenericDialog(7, action3, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t510003_x9003(z1=150, goods1=2141, val1=14):
    """State 0,18"""
    # goods:151:Estus Flask, goods:153:Estus Flask+1, goods:155:Estus Flask+2, goods:157:Estus Flask+3, goods:159:Estus Flask+4, goods:161:Estus Flask+5, goods:163:Estus Flask+6, goods:165:Estus Flask+7, goods:167:Estus Flask+8, goods:169:Estus Flask+9, goods:171:Estus Flask+10, goods:150:Estus Flask, goods:152:Estus Flask+1, goods:154:Estus Flask+2, goods:156:Estus Flask+3, goods:158:Estus Flask+4, goods:160:Estus Flask+5, goods:162:Estus Flask+6, goods:164:Estus Flask+7, goods:166:Estus Flask+8, goods:168:Estus Flask+9, goods:170:Estus Flask+10
    call = t510003_x9005(goods2=150, goods3=0)
    if call.Get() == 1:
        """State 10,19"""
        # goods:191:Ashen Estus Flask, goods:193:Ashen Estus Flask+1, goods:195:Ashen Estus Flask+2, goods:197:Ashen Estus Flask+3, goods:199:Ashen Estus Flask+4, goods:201:Ashen Estus Flask+5, goods:203:Ashen Estus Flask+6, goods:205:Ashen Estus Flask+7, goods:207:Ashen Estus Flask+8, goods:209:Ashen Estus Flask+9, goods:211:Ashen Estus Flask+10, goods:190:Ashen Estus Flask, goods:192:Ashen Estus Flask+1, goods:194:Ashen Estus Flask+2, goods:196:Ashen Estus Flask+3, goods:198:Ashen Estus Flask+4, goods:200:Ashen Estus Flask+5, goods:202:Ashen Estus Flask+6, goods:204:Ashen Estus Flask+7, goods:206:Ashen Estus Flask+8, goods:208:Ashen Estus Flask+9, goods:210:Ashen Estus Flask+10
        call = t510003_x9005(goods2=150, goods3=1)
        if call.Get() == 1:
            """State 12,9"""
            if GetEstusAllocation(0) + GetEstusAllocation(1) < val1:
                """State 1"""
                # goods:2141:Estus Shard
                if ComparePlayerInventoryNumber(3, goods1, 2, 0, 0) == 1:
                    """State 2,14"""
                    # action:12002003:"Use <?gdsparam@2141?> to reinforce Estus Flask?"
                    call = t510003_x9006(action2=12002003)
                    if call.Get() == 0:
                        """State 4,6"""
                        # goods:2141:Estus Shard
                        PlayerEquipmentQuantityChange(3, goods1, -1)
                        """State 7"""
                        EstusAllocationUpdate(GetEstusAllocation(0) + 1, 0)
                        """State 16"""
                        # action:13002010:"Reinforced Estus Flask, increasing number of uses\n"
                        assert t510003_x9007(action1=13002010)
                        """State 22"""
                        assert t510003_x9008(val2=14)
                    elif call.Done():
                        """State 5"""
                        pass
                else:
                    """State 3,15"""
                    # action:13002011:"No <?gdsparam@2141?> in inventory"
                    assert t510003_x9007(action1=13002011)
            else:
                """State 8,17"""
                # action:13002012:"Cannot reinforce further"
                assert t510003_x9007(action1=13002012)
        elif call.Done():
            """State 13,21"""
            # action:13002014:"No <?gdsparam@190?> in inventory"
            assert t510003_x9007(action1=13002014)
    elif call.Done():
        """State 11,20"""
        # action:13002013:"No <?gdsparam@150?> in inventory"
        assert t510003_x9007(action1=13002013)
    """State 23"""
    return 0

def t510003_x9004(z2=150):
    """State 0,6"""
    # goods:151:Estus Flask, goods:153:Estus Flask+1, goods:155:Estus Flask+2, goods:157:Estus Flask+3, goods:159:Estus Flask+4, goods:161:Estus Flask+5, goods:163:Estus Flask+6, goods:165:Estus Flask+7, goods:167:Estus Flask+8, goods:169:Estus Flask+9, goods:171:Estus Flask+10, goods:150:Estus Flask, goods:152:Estus Flask+1, goods:154:Estus Flask+2, goods:156:Estus Flask+3, goods:158:Estus Flask+4, goods:160:Estus Flask+5, goods:162:Estus Flask+6, goods:164:Estus Flask+7, goods:166:Estus Flask+8, goods:168:Estus Flask+9, goods:170:Estus Flask+10
    call = t510003_x9005(goods2=150, goods3=0)
    if call.Get() == 1:
        """State 1,7"""
        # goods:191:Ashen Estus Flask, goods:193:Ashen Estus Flask+1, goods:195:Ashen Estus Flask+2, goods:197:Ashen Estus Flask+3, goods:199:Ashen Estus Flask+4, goods:201:Ashen Estus Flask+5, goods:203:Ashen Estus Flask+6, goods:205:Ashen Estus Flask+7, goods:207:Ashen Estus Flask+8, goods:209:Ashen Estus Flask+9, goods:211:Ashen Estus Flask+10, goods:190:Ashen Estus Flask, goods:192:Ashen Estus Flask+1, goods:194:Ashen Estus Flask+2, goods:196:Ashen Estus Flask+3, goods:198:Ashen Estus Flask+4, goods:200:Ashen Estus Flask+5, goods:202:Ashen Estus Flask+6, goods:204:Ashen Estus Flask+7, goods:206:Ashen Estus Flask+8, goods:208:Ashen Estus Flask+9, goods:210:Ashen Estus Flask+10
        call = t510003_x9005(goods2=150, goods3=1)
        if call.Get() == 1:
            """State 3,4"""
            OpenEstusAllotMenu()
            assert not (CheckSpecificPersonMenuIsOpen(14, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif call.Done():
            """State 5,9"""
            # action:13002014:"No <?gdsparam@190?> in inventory"
            assert t510003_x9007(action1=13002014)
    elif call.Done():
        """State 2,8"""
        # action:13002013:"No <?gdsparam@150?> in inventory"
        assert t510003_x9007(action1=13002013)
    """State 10"""
    return 0

def t510003_x9005(goods2=150, goods3=_):
    """State 0,1"""
    if (not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 0 * 2) and not IsEquipmentIDObtained(3,
        goods2 + 1 + goods3 * 40 + 1 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 +
        2 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 3 * 2) and not IsEquipmentIDObtained(3,
        goods2 + 1 + goods3 * 40 + 4 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 +
        5 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 6 * 2) and not IsEquipmentIDObtained(3,
        goods2 + 1 + goods3 * 40 + 7 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 +
        8 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 9 * 2)):
        """State 2"""
        if (not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 10 * 2) and not IsEquipmentIDObtained(3,
            goods2 + 1 + goods3 * 40 + 11 * 2) and not IsEquipmentIDObtained(3, goods2 + 12 + goods3
            * 40 + 12 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 13 * 2) and not
            IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 14 * 2) and not IsEquipmentIDObtained(3,
            goods2 + 1 + goods3 * 40 + 15 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 *
            40 + 16 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 17 * 2) and not
            IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 18 * 2) and not IsEquipmentIDObtained(3,
            goods2 + 1 + goods3 * 40 + 19 * 2)):
            """State 3"""
            if (not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 0 * 2) and not IsEquipmentIDObtained(3,
                goods2 + 0 + goods3 * 40 + 1 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3
                * 40 + 2 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 3 * 2) and
                not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 4 * 2) and not IsEquipmentIDObtained(3,
                goods2 + 0 + goods3 * 40 + 5 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3
                * 40 + 6 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 7 * 2) and
                not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 8 * 2) and not IsEquipmentIDObtained(3,
                goods2 + 0 + goods3 * 40 + 9 * 2)):
                """State 4"""
                if (not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 10 * 2) and not IsEquipmentIDObtained(3,
                    goods2 + 0 + goods3 * 40 + 11 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 +
                    goods3 * 40 + 12 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 +
                    13 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 14 * 2) and not
                    IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 15 * 2) and not IsEquipmentIDObtained(3,
                    goods2 + 0 + goods3 * 40 + 16 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 +
                    goods3 * 40 + 17 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 +
                    18 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 19 * 2)):
                    """State 5"""
                    return 0
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass
    """State 6"""
    return 1

def t510003_x9006(action2=12002003):
    """State 0,1"""
    # action:12002003:"Use <?gdsparam@2141?> to reinforce Estus Flask?"
    OpenGenericDialog(8, action2, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t510003_x9007(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t510003_x9008(val2=14):
    """State 0,3"""
    if GetEstusAllocation(0) + GetEstusAllocation(1) < val2:
        """State 2"""
        pass
    else:
        """State 1,4"""
        RequestUnlockTrophy(16)
    """State 5"""
    return 0

def t510003_x9999():
    """State 0"""
    assert GetCurrentStateElapsedTime() > 0.1
    while True:
        """State 1"""
        MainBonfireMenuFlag()
        ClearTalkListData()
        # action:15002000:"Level Up"
        AddTalkListData(1, 15002000, -1)
        # action:15011020:"Purchase Item"
        AddTalkListData(2, 15011020, -1)
        # action:15000012:"Sell Item"
        AddTalkListData(3, 15000012, -1)
        # action:15010002:"Reinforce Weapon"
        AddTalkListData(4, 15010002, -1)
        # action:15010001:"Infuse Weapon"
        AddTalkListData(5, 15010001, -1)
        # action:15010003:"Repair Equipment"
        AddTalkListData(6, 15010003, -1)
        # action:15002002:"Allot Estus"
        AddTalkListData(7, 15002002, -1)
        # action:15002003:"Reinforce Estus Flask"
        AddTalkListData(8, 15002003, -1)
        AddTalkListData(9, 15027010, -1)
        AddTalkListData(10, 15027011, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        ShowShopMessage(1)
        if GetTalkListEntryResult() == 1:
            """State 2"""
            OpenSoul()
            assert not (CheckSpecificPersonMenuIsOpen(10, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 3"""
            OpenRegularShop(110000, 119899)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 4"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 4:
            """State 7"""
            if GetEventStatus(2051) == 1 or IsMultiplayerInProgress() == 1:
                """State 21,27"""
                assert t510003_x9002(action3=13010000)
            else:
                """State 17"""
                CombineMenuFlagAndEventFlag(6001, 232)
                CombineMenuFlagAndEventFlag(6001, 233)
                CombineMenuFlagAndEventFlag(6001, 234)
                """State 9"""
                OpenEnhanceShop(0)
                assert not (CheckSpecificPersonMenuIsOpen(9, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 5:
            """State 8"""
            CombineMenuFlagAndEventFlag(6001, 344)
            CombineMenuFlagAndEventFlag(6001, 337)
            CombineMenuFlagAndEventFlag(6001, 334)
            CombineMenuFlagAndEventFlag(300, 332)
            CombineMenuFlagAndEventFlag(300, 333)
            CombineMenuFlagAndEventFlag(300, 342)
            CombineMenuFlagAndEventFlag(301, 335)
            CombineMenuFlagAndEventFlag(301, 345)
            CombineMenuFlagAndEventFlag(301, 340)
            CombineMenuFlagAndEventFlag(302, 336)
            CombineMenuFlagAndEventFlag(302, 338)
            CombineMenuFlagAndEventFlag(302, 339)
            CombineMenuFlagAndEventFlag(303, 341)
            CombineMenuFlagAndEventFlag(303, 343)
            CombineMenuFlagAndEventFlag(303, 346)
            CombineMenuFlagAndEventFlag(6000, 347)
            CombineMenuFlagAndEventFlag(6001, 331)
            """State 6"""
            OpenEquipmentChangeOfPurposeShop()
            assert not (CheckSpecificPersonMenuIsOpen(7, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 6:
            """State 10"""
            OpenRepairShop()
            assert not (CheckSpecificPersonMenuIsOpen(8, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 7:
            """State 20,26"""
            assert t510003_x9004(z2=150) and not (CheckSpecificPersonMenuIsOpen(8, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 8:
            """State 19,25"""
            # goods:2141:Estus Shard
            assert (t510003_x9003(z1=150, goods1=2141, val1=14) and not (CheckSpecificPersonMenuIsOpen(8,
                    0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)))
        elif GetTalkListEntryResult() == 9:
            ReallocateAttributes()
            ClearTalkActionState()
            def ExitPause():
                SetEventState(73500161, 0)
            assert not (CheckSpecificPersonMenuIsOpen(19, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 10:
            OpenCharaMakeMenu()
            ClearTalkActionState()
            def ExitPause():
                SetEventState(73500161, 0)
            assert not (CheckSpecificPersonMenuIsOpen(16, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif (GetTalkListEntryResult() == 99 or not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not
              CheckSpecificPersonGenericDialogIsOpen(0))):
            """State 5,22"""
            return 0