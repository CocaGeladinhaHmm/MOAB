# -*- coding: utf-8 -*-
def t400000_1():
    """State 0,1"""
    t400000_x7()
    Quit()

def t400000_x0(action6=_):
    """State 0,1"""
    OpenGenericDialog(8, action6, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t400000_x1():
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

def t400000_x2(gesture1=17, z6=9019, flag3=6067):
    """State 0,1"""
    if GetEventStatus(flag3) == 1:
        """State 2"""
        pass
    else:
        """State 3,4"""
        AcquireGesture(gesture1)
        OpenItemAcquisitionMenu(3, z6, 1)
        SetEventState(flag3, 1)
        assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t400000_x3(actionbutton1=_, flag1=6001, flag2=_):
    """State 0"""
    while True:
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
                and not IsPlayerDead() and not IsCharacterDisabled())
        """State 2"""
        assert CompareBonfireState(1)
        """State 4"""
        if GetEventStatus(flag2) == 1:
            """State 5"""
            assert GetEventStatus(flag1) == 1 and not GetEventStatus(flag2)
            """State 6"""
            assert GetCurrentStateElapsedTime() > 1
        elif GetEventStatus(flag1) == 1 and not GetEventStatus(flag2):
            pass
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
    """State 7"""
    return 0

def t400000_x4(action5=_):
    """State 0,1"""
    OpenGenericDialog(7, action5, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t400000_x5(action4=10010713):
    """State 0,1"""
    # action:10010713:"Game installation incomplete.\nCannot travel between bonfires."
    OpenGenericDialog(1, action4, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t400000_x6(goods4=150, goods9=_):
    """State 0,1"""
    if (not IsEquipmentIDObtained(3, goods4 + 1 + goods9 * 40 + 0 * 2) and not IsEquipmentIDObtained(3,
        goods4 + 1 + goods9 * 40 + 1 * 2) and not IsEquipmentIDObtained(3, goods4 + 1 + goods9 * 40 +
        2 * 2) and not IsEquipmentIDObtained(3, goods4 + 1 + goods9 * 40 + 3 * 2) and not IsEquipmentIDObtained(3,
        goods4 + 1 + goods9 * 40 + 4 * 2) and not IsEquipmentIDObtained(3, goods4 + 1 + goods9 * 40 +
        5 * 2) and not IsEquipmentIDObtained(3, goods4 + 1 + goods9 * 40 + 6 * 2) and not IsEquipmentIDObtained(3,
        goods4 + 1 + goods9 * 40 + 7 * 2) and not IsEquipmentIDObtained(3, goods4 + 1 + goods9 * 40 +
        8 * 2) and not IsEquipmentIDObtained(3, goods4 + 1 + goods9 * 40 + 9 * 2)):
        """State 2"""
        if (not IsEquipmentIDObtained(3, goods4 + 1 + goods9 * 40 + 10 * 2) and not IsEquipmentIDObtained(3,
            goods4 + 1 + goods9 * 40 + 11 * 2) and not IsEquipmentIDObtained(3, goods4 + 12 + goods9
            * 40 + 12 * 2) and not IsEquipmentIDObtained(3, goods4 + 1 + goods9 * 40 + 13 * 2) and not
            IsEquipmentIDObtained(3, goods4 + 1 + goods9 * 40 + 14 * 2) and not IsEquipmentIDObtained(3,
            goods4 + 1 + goods9 * 40 + 15 * 2) and not IsEquipmentIDObtained(3, goods4 + 1 + goods9 *
            40 + 16 * 2) and not IsEquipmentIDObtained(3, goods4 + 1 + goods9 * 40 + 17 * 2) and not
            IsEquipmentIDObtained(3, goods4 + 1 + goods9 * 40 + 18 * 2) and not IsEquipmentIDObtained(3,
            goods4 + 1 + goods9 * 40 + 19 * 2)):
            """State 3"""
            if (not IsEquipmentIDObtained(3, goods4 + 0 + goods9 * 40 + 0 * 2) and not IsEquipmentIDObtained(3,
                goods4 + 0 + goods9 * 40 + 1 * 2) and not IsEquipmentIDObtained(3, goods4 + 0 + goods9
                * 40 + 2 * 2) and not IsEquipmentIDObtained(3, goods4 + 0 + goods9 * 40 + 3 * 2) and
                not IsEquipmentIDObtained(3, goods4 + 0 + goods9 * 40 + 4 * 2) and not IsEquipmentIDObtained(3,
                goods4 + 0 + goods9 * 40 + 5 * 2) and not IsEquipmentIDObtained(3, goods4 + 0 + goods9
                * 40 + 6 * 2) and not IsEquipmentIDObtained(3, goods4 + 0 + goods9 * 40 + 7 * 2) and
                not IsEquipmentIDObtained(3, goods4 + 0 + goods9 * 40 + 8 * 2) and not IsEquipmentIDObtained(3,
                goods4 + 0 + goods9 * 40 + 9 * 2)):
                """State 4"""
                if (not IsEquipmentIDObtained(3, goods4 + 0 + goods9 * 40 + 10 * 2) and not IsEquipmentIDObtained(3,
                    goods4 + 0 + goods9 * 40 + 11 * 2) and not IsEquipmentIDObtained(3, goods4 + 0 +
                    goods9 * 40 + 12 * 2) and not IsEquipmentIDObtained(3, goods4 + 0 + goods9 * 40 +
                    13 * 2) and not IsEquipmentIDObtained(3, goods4 + 0 + goods9 * 40 + 14 * 2) and not
                    IsEquipmentIDObtained(3, goods4 + 0 + goods9 * 40 + 15 * 2) and not IsEquipmentIDObtained(3,
                    goods4 + 0 + goods9 * 40 + 16 * 2) and not IsEquipmentIDObtained(3, goods4 + 0 +
                    goods9 * 40 + 17 * 2) and not IsEquipmentIDObtained(3, goods4 + 0 + goods9 * 40 +
                    18 * 2) and not IsEquipmentIDObtained(3, goods4 + 0 + goods9 * 40 + 19 * 2)):
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

def t400000_x7():
    """State 0,1"""
    t400000_x8()
    Quit()
    """Unused"""
    """State 2"""
    t400000_x11()
    Quit()
    """State 3"""
    return 0

def t400000_x8():
    """State 0,1"""
    if CompareBonfireLevel(5, 0) == 1:
        """State 2"""
        Label('L0')
    else:
        """State 3,20"""
        call = t400000_x3(actionbutton1=6100, flag1=6001, flag2=74000010)
        if call.Done():
            """State 7"""
            TurnCharacterToFaceEntity(-1, 10000, -1)
            assert GetWhetherChrEventAnimHasEnded(10000) == 1 and GetCurrentStateElapsedFrames() > 1
            """State 4"""
            OfferHumanity()
            assert CompareBonfireLevel(5, 0) == 1
            """State 10"""
            UpdatePlayerRespawnPoint()
            """State 12"""
            RequestUnlockTrophy(41)
            """State 9"""
            SetEventState(13000000, 1)
            Goto('L0')
        elif CompareBonfireLevel(5, 0) == 1:
            """State 13"""
            RequestUnlockTrophy(41)
            """State 14"""
            SetEventState(13000000, 1)
    while True:
        """State 19"""
        call = t400000_x3(actionbutton1=6102, flag1=6001, flag2=74000010)
        if call.Done():
            break
        elif GetEventStatus(14000618) == 1 and GetEventStatus(6500) == 1:
            """State 16"""
            if (GetIsOnline() == 1 and not GetIsNetPenalizedForArena() and CompareBonfireState(1) and
                not GetEventStatus(74000010)):
                """State 21"""
                TurnCharacterToFaceEntity(68011, 10000, -1)
                call = t400000_x12()
                def ExitPause():
                    TurnCharacterToFaceEntity(68012, 10000, -1)
                    SetEventState(14005617, 0)
                    SetEventState(14000618, 0)
                if call.Done():
                    Goto('L0')
                elif (HasPlayerBeenAttacked() == 1 or GetDistanceToPlayer() > 3 or CompareBonfireState(0)
                      or IsPlayerDead() == 1):
                    pass
            else:
                """State 15"""
                SetEventState(14000618, 0)
                SetEventState(14005617, 0)
                continue
        """State 18"""
        Label('L1')
        assert t400000_x14()
        Goto('L0')
    """State 5"""
    ClearPlayerDamageInfo()
    """State 6"""
    SetTalkTime(1)
    """State 8"""
    TurnCharacterToFaceEntity(-1, 10000, -1)
    assert GetWhetherChrEventAnimHasEnded(10000) == 1 and GetCurrentStateElapsedFrames() > 1
    """State 11"""
    UpdatePlayerRespawnPoint()
    """State 17"""
    StartBonfireAnimLoop()
    call = t400000_x12()
    def ExitPause():
        EndBonfireKindleAnimLoop()
        SetEventState(14005617, 0)
        SetEventState(14000618, 0)
    if call.Done():
        Goto('L0')
    elif (HasPlayerBeenAttacked() == 1 or GetDistanceToPlayer() > 3 or CompareBonfireState(0) or IsPlayerDead()
          == 1):
        Goto('L1')
    """Unused"""
    """State 22"""
    return 0

def t400000_x9():
    """State 0,4"""
    call = t400000_x1()
    if call.Done() and CompareBonfireLevel(5, 0) == 1:
        pass
    elif call.Done():
        """State 2,5"""
        call = t400000_x3(actionbutton1=6100, flag1=6001, flag2=6000)
        if call.Done():
            """State 3"""
            OfferHumanity()
            assert CompareBonfireLevel(5, 0) == 1
        elif CompareBonfireLevel(5, 0) == 1:
            pass
    """State 1"""
    Quit()
    """Unused"""
    """State 6"""
    return 0

def t400000_x10():
    """State 0,1"""
    assert t400000_x1()
    """State 2"""
    return 0

def t400000_x11():
    """State 0"""
    while True:
        """State 1"""
        call = t400000_x9()
        assert IsClientPlayer() == 1
        """State 2"""
        call = t400000_x10()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t400000_x12():
    """State 0,33"""
    if (GetEventStatus(14000618) == 1 and GetEventStatus(6500) == 1 and (GetEventStatus(6951) == 1 or
        GetEventStatus(6952) == 1)):
        """State 32,44"""
        SetEventState(14000618, 0)
        assert (GetCurrentStateElapsedTime() > 2 and not (CheckSpecificPersonMenuIsOpen(-1, 2) == 1 and
                not CheckSpecificPersonGenericDialogIsOpen(2)) and not CheckSpecificPersonGenericDialogIsOpen(2))
        """State 43,30"""
        Label('L0')
        if not GetIsOnline():
            """State 37,56"""
            assert t400000_x4(action5=13000060)
        elif GetIsNetPenalizedForArena() == 1:
            """State 38,55"""
            assert t400000_x4(action5=13000061)
        else:
            """State 31"""
            UndeadMatch()
            def WhilePaused():
                SetEventState(14005617, 1)
            assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                    2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
    else:
        """State 11"""
        assert GetCurrentStateElapsedTime() > 2
        """State 50"""
        assert t400000_x2(gesture1=17, z6=9019, flag3=6067)
        """State 51"""
        # goods:150:Estus Flask, goods:151:Estus Flask, goods:190:Ashen Estus Flask, goods:191:Ashen Estus Flask, goods:152:Estus Flask+1, goods:153:Estus Flask+1, goods:192:Ashen Estus Flask+1, goods:193:Ashen Estus Flask+1, goods:154:Estus Flask+2, goods:155:Estus Flask+2, goods:194:Ashen Estus Flask+2, goods:195:Ashen Estus Flask+2, goods:156:Estus Flask+3, goods:157:Estus Flask+3, goods:196:Ashen Estus Flask+3, goods:197:Ashen Estus Flask+3, goods:158:Estus Flask+4, goods:159:Estus Flask+4, goods:198:Ashen Estus Flask+4, goods:199:Ashen Estus Flask+4, goods:160:Estus Flask+5, goods:161:Estus Flask+5, goods:200:Ashen Estus Flask+5, goods:201:Ashen Estus Flask+5, goods:162:Estus Flask+6, goods:163:Estus Flask+6, goods:202:Ashen Estus Flask+6, goods:203:Ashen Estus Flask+6, goods:164:Estus Flask+7, goods:165:Estus Flask+7, goods:204:Ashen Estus Flask+7, goods:205:Ashen Estus Flask+7, goods:166:Estus Flask+8, goods:167:Estus Flask+8, goods:206:Ashen Estus Flask+8, goods:207:Ashen Estus Flask+8, goods:168:Estus Flask+9, goods:169:Estus Flask+9, goods:208:Ashen Estus Flask+9, goods:209:Ashen Estus Flask+9, goods:170:Estus Flask+10, goods:171:Estus Flask+10, goods:210:Ashen Estus Flask+10, goods:211:Ashen Estus Flask+10
        assert t400000_x19(goods4=150, z3=10, z4=11)
        """State 23"""
        MainBonfireMenuFlag()
    while True:
        """State 1"""
        ClearTalkListData()
        """State 2"""
        # action:15000150:"Travel"
        AddTalkListData(1, 15000150, -1)
        # action:15000130:"Attune Spell"
        AddTalkListData(4, 15000130, -1)
        # action:15000220:"Organize Storage Box"
        AddTalkListData(2, 15000220, -1)
        # action:15000160:"Burn <?gdsparam@2143?>"
        AddTalkListData(7, 15000160, -1)
        # action:15000331:"Begin journey <?nextLoopCount?>"
        AddTalkListDataIf(GetEventStatus(9920) == 1 or GetEventStatus(9921) == 1 or GetEventStatus(9922) == 1 or GetEventStatus(9923) == 1,
                          6, 15000331, -1)
        AddTalkListDataIf(not GetEventStatus(6500) and ComparePlayerInventoryNumber(3, 2153, 4, 1, 0) == 1 and (GetEventStatus(6951) == 1 or GetEventStatus(6952) == 1),
                          8, 15000340, -1)
        AddTalkListDataIf(GetEventStatus(6500) == 1 and (GetEventStatus(6951) == 1 or GetEventStatus(6952) == 1),
                          8, 15000350, -1)
        AddTalkListData(98, 80000001, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        """State 5"""
        ShowShopMessage(1)
        def WhilePaused():
            SetEventStateIf(not GetEventStatus(14005617) and (GetEventStatus(2051) == 1 or IsMultiplayerInProgress() == 1),
                            14005617, 1)
        if GetTalkListEntryResult() == 2:
            """State 4"""
            ForceCloseMenu()
            """State 15"""
            OpenRepository()
            assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                    2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
            continue
        elif GetTalkListEntryResult() == 1:
            """State 3"""
            if GetEventStatus(2051) == 1 or IsMultiplayerInProgress() == 1:
                """State 34,52"""
                assert t400000_x4(action5=13000070)
                continue
            elif GetEventStatus(2030) == 1:
                """State 25"""
                if not GetEventStatus(131):
                    """State 27,9"""
                    StartWarpMenuInit(3001960)
                else:
                    """State 26,28"""
                    StartWarpMenuInit(-1)
                """State 29"""
                SetEventState(14005617, 0)
                assert not (CheckSpecificPersonMenuIsOpen(2, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                """State 13"""
                if WasWarpMenuDestinationSelected() == 1:
                    """State 12,10"""
                    assert GetCurrentStateElapsedTime() > 10
                else:
                    """State 14"""
                    continue
            else:
                """State 24,48"""
                # action:10010713:"Game installation incomplete.\nCannot travel between bonfires."
                assert t400000_x5(action4=10010713)
                continue
        elif GetTalkListEntryResult() == 4:
            """State 7,8"""
            OpenMagicEquip(1000, 1000)
            assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                    2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
            continue
        elif GetTalkListEntryResult() == 6:
            """State 16"""
            if GetEventStatus(2051) == 1 or IsMultiplayerInProgress() == 1:
                """State 36,54"""
                assert t400000_x4(action5=13000072)
                continue
            else:
                """State 46"""
                # action:12000300:"If you begin journey <?nextLoopCount?>,\nyou will not be able to return to journey <?loopCount?>.\nAre you sure you wish to begin journey <?nextLoopCount?>?"
                call = t400000_x0(action6=12000300)
                if call.Get() == 0:
                    """State 20,18"""
                    SetEventState(74000012, 1)
                    SetEventState(14005617, 0)
                    """State 17"""
                    assert GetCurrentStateElapsedTime() > 10
                    Goto('L2')
                elif call.Get() == 1:
                    pass
                """State 19"""
                Label('L1')
                continue
        elif GetTalkListEntryResult() == 99 or not GetTalkListEntryResult():
            """State 6"""
            pass
        elif GetTalkListEntryResult() == 7:
            """State 22"""
            if GetEventStatus(2051) == 1:
                """State 35,53"""
                assert t400000_x4(action5=13000071)
                continue
            else:
                """State 49"""
                # goods:2143:Undead Bone Shard
                assert t400000_x13(goods5=2143, val3=11)
                continue
        elif GetTalkListEntryResult() == 8 and (GetEventStatus(6951) == 1 or GetEventStatus(6952) == 1):
            """State 39"""
            if not GetEventStatus(6500):
                """State 42,41"""
                SetEventState(6500, 1)
                """State 57"""
                assert t400000_x20()
                """State 40"""
                PlayerEquipmentQuantityChange(3, 2153, -1)
                assert GetCurrentStateElapsedTime() > 2
                continue
            else:
                Goto('L0')
        elif GetTalkListEntryResult() == 98:
            """State 59"""
            assert t400000_x9999()
        elif not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 45"""
            assert (not (CheckSpecificPersonMenuIsOpen(-1, 2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2))
                    and not CheckSpecificPersonGenericDialogIsOpen(2))
            continue
        """State 58"""
        Label('L2')
        return 0
    """Unused"""
    """State 21"""
    Label('L3')
    Quit()
    """State 47"""
    # action:99000101:""
    call = t400000_x0(action6=99000101)
    if call.Get() == 0:
        Goto('L3')
    elif call.Get() == 1:
        Goto('L1')

def t400000_x13(goods5=2143, val3=11):
    """State 0,6"""
    if GetTotalBonfireLevel() <= val3:
        """State 5"""
        # goods:2143:Undead Bone Shard
        if ComparePlayerInventoryNumber(3, goods5, 2, 0, 0) == 1:
            """State 1,10"""
            # action:12000200:"Burn <?gdsparam@2143?>?"
            call = t400000_x0(action6=12000200)
            if call.Get() == 0:
                """State 3,8"""
                BonfireActivation(GetTotalBonfireLevel() + 1)
                """State 9"""
                # goods:2143:Undead Bone Shard
                PlayerEquipmentQuantityChange(3, goods5, -1)
                """State 13"""
                # goods:150:Estus Flask, goods:151:Estus Flask, goods:190:Ashen Estus Flask, goods:191:Ashen Estus Flask, goods:152:Estus Flask+1, goods:153:Estus Flask+1, goods:192:Ashen Estus Flask+1, goods:193:Ashen Estus Flask+1, goods:154:Estus Flask+2, goods:155:Estus Flask+2, goods:194:Ashen Estus Flask+2, goods:195:Ashen Estus Flask+2, goods:156:Estus Flask+3, goods:157:Estus Flask+3, goods:196:Ashen Estus Flask+3, goods:197:Ashen Estus Flask+3, goods:158:Estus Flask+4, goods:159:Estus Flask+4, goods:198:Ashen Estus Flask+4, goods:199:Ashen Estus Flask+4, goods:160:Estus Flask+5, goods:161:Estus Flask+5, goods:200:Ashen Estus Flask+5, goods:201:Ashen Estus Flask+5, goods:162:Estus Flask+6, goods:163:Estus Flask+6, goods:202:Ashen Estus Flask+6, goods:203:Ashen Estus Flask+6, goods:164:Estus Flask+7, goods:165:Estus Flask+7, goods:204:Ashen Estus Flask+7, goods:205:Ashen Estus Flask+7, goods:166:Estus Flask+8, goods:167:Estus Flask+8, goods:206:Ashen Estus Flask+8, goods:207:Ashen Estus Flask+8, goods:168:Estus Flask+9, goods:169:Estus Flask+9, goods:208:Ashen Estus Flask+9, goods:209:Ashen Estus Flask+9, goods:170:Estus Flask+10, goods:171:Estus Flask+10, goods:210:Ashen Estus Flask+10, goods:211:Ashen Estus Flask+10
                assert t400000_x15(goods6=150, z5=10, val3=val3) and GetCurrentStateElapsedTime() > 2
            elif call.Get() == 1:
                """State 4"""
                pass
        else:
            """State 2,12"""
            # action:13000201:"No <?gdsparam@2143?> in inventory"
            assert t400000_x4(action5=13000201)
    else:
        """State 7,11"""
        # action:13000200:"Cannot kindle any further"
        assert t400000_x4(action5=13000200)
    """State 14"""
    return 0

def t400000_x14():
    """State 0,1"""
    assert t400000_x1()
    """State 2"""
    return 0

def t400000_x15(goods6=150, z5=10, val3=11):
    """State 0,5"""
    # goods:151:Estus Flask, goods:153:Estus Flask+1, goods:155:Estus Flask+2, goods:157:Estus Flask+3, goods:159:Estus Flask+4, goods:161:Estus Flask+5, goods:163:Estus Flask+6, goods:165:Estus Flask+7, goods:167:Estus Flask+8, goods:169:Estus Flask+9, goods:171:Estus Flask+10, goods:150:Estus Flask, goods:152:Estus Flask+1, goods:154:Estus Flask+2, goods:156:Estus Flask+3, goods:158:Estus Flask+4, goods:160:Estus Flask+5, goods:162:Estus Flask+6, goods:164:Estus Flask+7, goods:166:Estus Flask+8, goods:168:Estus Flask+9, goods:170:Estus Flask+10
    call = t400000_x6(goods4=goods6, goods9=0)
    if call.Get() == 1:
        """State 1,7"""
        # goods:150:Estus Flask, goods:152:Estus Flask+1, goods:154:Estus Flask+2, goods:156:Estus Flask+3, goods:158:Estus Flask+4, goods:160:Estus Flask+5, goods:162:Estus Flask+6, goods:164:Estus Flask+7, goods:166:Estus Flask+8, goods:168:Estus Flask+9, goods:170:Estus Flask+10
        assert t400000_x16(goods4=goods6, goods7=0, goods8=0)
        """State 8"""
        # goods:151:Estus Flask, goods:153:Estus Flask+1, goods:155:Estus Flask+2, goods:157:Estus Flask+3, goods:159:Estus Flask+4, goods:161:Estus Flask+5, goods:163:Estus Flask+6, goods:165:Estus Flask+7, goods:167:Estus Flask+8, goods:169:Estus Flask+9, goods:171:Estus Flask+10
        assert t400000_x16(goods4=goods6, goods7=0, goods8=1)
    elif call.Done():
        """State 2"""
        pass
    """State 6"""
    # goods:191:Ashen Estus Flask, goods:193:Ashen Estus Flask+1, goods:195:Ashen Estus Flask+2, goods:197:Ashen Estus Flask+3, goods:199:Ashen Estus Flask+4, goods:201:Ashen Estus Flask+5, goods:203:Ashen Estus Flask+6, goods:205:Ashen Estus Flask+7, goods:207:Ashen Estus Flask+8, goods:209:Ashen Estus Flask+9, goods:211:Ashen Estus Flask+10, goods:190:Ashen Estus Flask, goods:192:Ashen Estus Flask+1, goods:194:Ashen Estus Flask+2, goods:196:Ashen Estus Flask+3, goods:198:Ashen Estus Flask+4, goods:200:Ashen Estus Flask+5, goods:202:Ashen Estus Flask+6, goods:204:Ashen Estus Flask+7, goods:206:Ashen Estus Flask+8, goods:208:Ashen Estus Flask+9, goods:210:Ashen Estus Flask+10
    call = t400000_x6(goods4=goods6, goods9=1)
    if call.Get() == 1:
        """State 3,9"""
        # goods:190:Ashen Estus Flask, goods:192:Ashen Estus Flask+1, goods:194:Ashen Estus Flask+2, goods:196:Ashen Estus Flask+3, goods:198:Ashen Estus Flask+4, goods:200:Ashen Estus Flask+5, goods:202:Ashen Estus Flask+6, goods:204:Ashen Estus Flask+7, goods:206:Ashen Estus Flask+8, goods:208:Ashen Estus Flask+9, goods:210:Ashen Estus Flask+10
        assert t400000_x16(goods4=goods6, goods7=1, goods8=0)
        """State 10"""
        # goods:191:Ashen Estus Flask, goods:193:Ashen Estus Flask+1, goods:195:Ashen Estus Flask+2, goods:197:Ashen Estus Flask+3, goods:199:Ashen Estus Flask+4, goods:201:Ashen Estus Flask+5, goods:203:Ashen Estus Flask+6, goods:205:Ashen Estus Flask+7, goods:207:Ashen Estus Flask+8, goods:209:Ashen Estus Flask+9, goods:211:Ashen Estus Flask+10
        assert t400000_x16(goods4=goods6, goods7=1, goods8=1)
    elif call.Done():
        """State 4"""
        pass
    """State 11"""
    assert (t400000_x17(mode1=1, val4=2, val5=3, val6=4, val7=5, val8=6, val9=7, val10=8, val11=9, val12=10,
            val13=11))
    """State 12"""
    assert t400000_x18(val3=val3)
    """State 13"""
    return 0

def t400000_x16(goods4=150, goods7=_, goods8=_):
    """State 0,1"""
    if IsEquipmentIDObtained(3, goods4 + goods8 + goods7 * 40 + 0 * 2) == 1:
        """State 2"""
        ReplaceTool(goods4 + goods7 * 40 + 0 * 2 + goods8, goods4 + goods7 * 40 + goods8 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif IsEquipmentIDObtained(3, goods4 + goods8 + goods7 * 40 + 1 * 2) == 1:
        """State 3"""
        ReplaceTool(goods4 + goods7 * 40 + 1 * 2 + goods8, goods4 + goods7 * 40 + goods8 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif IsEquipmentIDObtained(3, goods4 + goods8 + goods7 * 40 + 2 * 2) == 1:
        """State 4"""
        ReplaceTool(goods4 + goods7 * 40 + 2 * 2 + goods8, goods4 + goods7 * 40 + goods8 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif IsEquipmentIDObtained(3, goods4 + goods8 + goods7 * 40 + 3 * 2) == 1:
        """State 5"""
        ReplaceTool(goods4 + goods7 * 40 + 3 * 2 + goods8, goods4 + goods7 * 40 + goods8 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif IsEquipmentIDObtained(3, goods4 + goods8 + goods7 * 40 + 4 * 2) == 1:
        """State 6"""
        ReplaceTool(goods4 + goods7 * 40 + 4 * 2 + goods8, goods4 + goods7 * 40 + goods8 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif IsEquipmentIDObtained(3, goods4 + goods8 + goods7 * 40 + 5 * 2) == 1:
        """State 7"""
        ReplaceTool(goods4 + goods7 * 40 + 5 * 2 + goods8, goods4 + goods7 * 40 + goods8 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif IsEquipmentIDObtained(3, goods4 + goods8 + goods7 * 40 + 6 * 2) == 1:
        """State 8"""
        ReplaceTool(goods4 + goods7 * 40 + 6 * 2 + goods8, goods4 + goods7 * 40 + goods8 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif IsEquipmentIDObtained(3, goods4 + goods8 + goods7 * 40 + 7 * 2) == 1:
        """State 9"""
        ReplaceTool(goods4 + goods7 * 40 + 7 * 2 + goods8, goods4 + goods7 * 40 + goods8 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif IsEquipmentIDObtained(3, goods4 + goods8 + goods7 * 40 + 8 * 2) == 1:
        """State 10"""
        ReplaceTool(goods4 + goods7 * 40 + 8 * 2 + goods8, goods4 + goods7 * 40 + goods8 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif IsEquipmentIDObtained(3, goods4 + goods8 + goods7 * 40 + 9 * 2) == 1:
        """State 11"""
        ReplaceTool(goods4 + goods7 * 40 + 9 * 2 + goods8, goods4 + goods7 * 40 + goods8 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif IsEquipmentIDObtained(3, goods4 + goods8 + goods7 * 40 + 10 * 2) == 1:
        """State 12"""
        ReplaceTool(goods4 + goods7 * 40 + 10 * 2 + goods8, goods4 + goods7 * 40 + goods8 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    else:
        """State 13"""
        pass
    """State 14"""
    return 0

def t400000_x17(mode1=1, val4=2, val5=3, val6=4, val7=5, val8=6, val9=7, val10=8, val11=9, val12=10, val13=11):
    """State 0,1"""
    if GetTotalBonfireLevel() <= mode1:
        """State 13"""
        Label('L0')
    else:
        """State 2"""
        SetEventState(6020, 1)
        if GetTotalBonfireLevel() <= val4:
            Goto('L0')
        else:
            """State 3"""
            SetEventState(6021, 1)
            if GetTotalBonfireLevel() <= val5:
                Goto('L0')
            else:
                """State 4"""
                SetEventState(6022, 1)
                if GetTotalBonfireLevel() <= val6:
                    Goto('L0')
                else:
                    """State 5"""
                    SetEventState(6023, 1)
                    if GetTotalBonfireLevel() <= val7:
                        Goto('L0')
                    else:
                        """State 6"""
                        SetEventState(6024, 1)
                        if GetTotalBonfireLevel() <= val8:
                            Goto('L0')
                        else:
                            """State 7"""
                            SetEventState(6025, 1)
                            if GetTotalBonfireLevel() <= val9:
                                Goto('L0')
                            else:
                                """State 8"""
                                SetEventState(6026, 1)
                                if GetTotalBonfireLevel() <= val10:
                                    Goto('L0')
                                else:
                                    """State 9"""
                                    SetEventState(6027, 1)
                                    if GetTotalBonfireLevel() <= val11:
                                        Goto('L0')
                                    else:
                                        """State 10"""
                                        SetEventState(6028, 1)
                                        if GetTotalBonfireLevel() <= val12:
                                            Goto('L0')
                                        else:
                                            """State 11"""
                                            SetEventState(6029, 1)
                                            if GetTotalBonfireLevel() <= val13:
                                                Goto('L0')
                                            else:
                                                """State 14"""
                                                SetEventState(6030, 1)
    """State 15"""
    return 0
    """Unused"""
    """State 12"""
    Quit()

def t400000_x18(val3=11):
    """State 0,3"""
    if GetTotalBonfireLevel() <= val3:
        """State 2"""
        pass
    else:
        """State 1,4"""
        RequestUnlockTrophy(15)
    """State 5"""
    return 0

def t400000_x19(goods4=150, z3=10, z4=11):
    """State 0,1"""
    if GetEventStatus(6030) == 1:
        """State 12"""
        BonfireActivation(11)
    elif GetEventStatus(6029) == 1:
        """State 11"""
        BonfireActivation(10)
    elif GetEventStatus(6028) == 1:
        """State 10"""
        BonfireActivation(9)
    elif GetEventStatus(6027) == 1:
        """State 9"""
        BonfireActivation(8)
    elif GetEventStatus(6026) == 1:
        """State 8"""
        BonfireActivation(7)
    elif GetEventStatus(6025) == 1:
        """State 7"""
        BonfireActivation(6)
    elif GetEventStatus(6024) == 1:
        """State 6"""
        BonfireActivation(5)
    elif GetEventStatus(6023) == 1:
        """State 5"""
        BonfireActivation(4)
    elif GetEventStatus(6022) == 1:
        """State 4"""
        BonfireActivation(3)
    elif GetEventStatus(6021) == 1:
        """State 3"""
        BonfireActivation(2)
    else:
        """State 2"""
        BonfireActivation(1)
    """State 13,19"""
    # goods:151:Estus Flask, goods:153:Estus Flask+1, goods:155:Estus Flask+2, goods:157:Estus Flask+3, goods:159:Estus Flask+4, goods:161:Estus Flask+5, goods:163:Estus Flask+6, goods:165:Estus Flask+7, goods:167:Estus Flask+8, goods:169:Estus Flask+9, goods:171:Estus Flask+10, goods:150:Estus Flask, goods:152:Estus Flask+1, goods:154:Estus Flask+2, goods:156:Estus Flask+3, goods:158:Estus Flask+4, goods:160:Estus Flask+5, goods:162:Estus Flask+6, goods:164:Estus Flask+7, goods:166:Estus Flask+8, goods:168:Estus Flask+9, goods:170:Estus Flask+10
    call = t400000_x6(goods4=goods4, goods9=0)
    if call.Get() == 1:
        """State 14,21"""
        # goods:150:Estus Flask, goods:152:Estus Flask+1, goods:154:Estus Flask+2, goods:156:Estus Flask+3, goods:158:Estus Flask+4, goods:160:Estus Flask+5, goods:162:Estus Flask+6, goods:164:Estus Flask+7, goods:166:Estus Flask+8, goods:168:Estus Flask+9, goods:170:Estus Flask+10
        assert t400000_x16(goods4=goods4, goods7=0, goods8=0)
        """State 22"""
        # goods:151:Estus Flask, goods:153:Estus Flask+1, goods:155:Estus Flask+2, goods:157:Estus Flask+3, goods:159:Estus Flask+4, goods:161:Estus Flask+5, goods:163:Estus Flask+6, goods:165:Estus Flask+7, goods:167:Estus Flask+8, goods:169:Estus Flask+9, goods:171:Estus Flask+10
        assert t400000_x16(goods4=goods4, goods7=0, goods8=1)
    elif call.Done():
        """State 15"""
        pass
    """State 20"""
    # goods:191:Ashen Estus Flask, goods:193:Ashen Estus Flask+1, goods:195:Ashen Estus Flask+2, goods:197:Ashen Estus Flask+3, goods:199:Ashen Estus Flask+4, goods:201:Ashen Estus Flask+5, goods:203:Ashen Estus Flask+6, goods:205:Ashen Estus Flask+7, goods:207:Ashen Estus Flask+8, goods:209:Ashen Estus Flask+9, goods:211:Ashen Estus Flask+10, goods:190:Ashen Estus Flask, goods:192:Ashen Estus Flask+1, goods:194:Ashen Estus Flask+2, goods:196:Ashen Estus Flask+3, goods:198:Ashen Estus Flask+4, goods:200:Ashen Estus Flask+5, goods:202:Ashen Estus Flask+6, goods:204:Ashen Estus Flask+7, goods:206:Ashen Estus Flask+8, goods:208:Ashen Estus Flask+9, goods:210:Ashen Estus Flask+10
    call = t400000_x6(goods4=goods4, goods9=1)
    if call.Get() == 1:
        """State 16,23"""
        # goods:190:Ashen Estus Flask, goods:192:Ashen Estus Flask+1, goods:194:Ashen Estus Flask+2, goods:196:Ashen Estus Flask+3, goods:198:Ashen Estus Flask+4, goods:200:Ashen Estus Flask+5, goods:202:Ashen Estus Flask+6, goods:204:Ashen Estus Flask+7, goods:206:Ashen Estus Flask+8, goods:208:Ashen Estus Flask+9, goods:210:Ashen Estus Flask+10
        assert t400000_x16(goods4=goods4, goods7=1, goods8=0)
        """State 24"""
        # goods:191:Ashen Estus Flask, goods:193:Ashen Estus Flask+1, goods:195:Ashen Estus Flask+2, goods:197:Ashen Estus Flask+3, goods:199:Ashen Estus Flask+4, goods:201:Ashen Estus Flask+5, goods:203:Ashen Estus Flask+6, goods:205:Ashen Estus Flask+7, goods:207:Ashen Estus Flask+8, goods:209:Ashen Estus Flask+9, goods:211:Ashen Estus Flask+10
        assert t400000_x16(goods4=goods4, goods7=1, goods8=1)
    elif call.Done():
        """State 17"""
        pass
    """State 18,25"""
    return 0

def t400000_x20():
    """State 0,1"""
    if GetTotalBonfireLevel() < 1:
        """State 2"""
        SetEventState(74000015, 1)
    elif GetTotalBonfireLevel() < 2:
        """State 3"""
        SetEventState(74000016, 1)
    elif GetTotalBonfireLevel() < 3:
        """State 4"""
        SetEventState(74000017, 1)
    elif GetTotalBonfireLevel() < 4:
        """State 5"""
        SetEventState(74000018, 1)
    elif GetTotalBonfireLevel() < 5:
        """State 6"""
        SetEventState(74000019, 1)
    elif GetTotalBonfireLevel() < 6:
        """State 7"""
        SetEventState(74000020, 1)
    elif GetTotalBonfireLevel() < 7:
        """State 8"""
        SetEventState(74000021, 1)
    elif GetTotalBonfireLevel() < 8:
        """State 9"""
        SetEventState(74000022, 1)
    elif GetTotalBonfireLevel() < 9:
        """State 10"""
        SetEventState(74000023, 1)
    elif GetTotalBonfireLevel() < 10:
        """State 11"""
        SetEventState(74000024, 1)
    else:
        """State 12"""
        SetEventState(74000025, 1)
    """State 13"""
    return 0

def t400000_x9002(action3=13010000):
    """State 0,1"""
    OpenGenericDialog(7, action3, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t400000_x9003(z1=150, goods1=2141, val1=14):
    """State 0,18"""
    # goods:151:Estus Flask, goods:153:Estus Flask+1, goods:155:Estus Flask+2, goods:157:Estus Flask+3, goods:159:Estus Flask+4, goods:161:Estus Flask+5, goods:163:Estus Flask+6, goods:165:Estus Flask+7, goods:167:Estus Flask+8, goods:169:Estus Flask+9, goods:171:Estus Flask+10, goods:150:Estus Flask, goods:152:Estus Flask+1, goods:154:Estus Flask+2, goods:156:Estus Flask+3, goods:158:Estus Flask+4, goods:160:Estus Flask+5, goods:162:Estus Flask+6, goods:164:Estus Flask+7, goods:166:Estus Flask+8, goods:168:Estus Flask+9, goods:170:Estus Flask+10
    call = t400000_x9005(goods2=150, goods3=0)
    if call.Get() == 1:
        """State 10,19"""
        # goods:191:Ashen Estus Flask, goods:193:Ashen Estus Flask+1, goods:195:Ashen Estus Flask+2, goods:197:Ashen Estus Flask+3, goods:199:Ashen Estus Flask+4, goods:201:Ashen Estus Flask+5, goods:203:Ashen Estus Flask+6, goods:205:Ashen Estus Flask+7, goods:207:Ashen Estus Flask+8, goods:209:Ashen Estus Flask+9, goods:211:Ashen Estus Flask+10, goods:190:Ashen Estus Flask, goods:192:Ashen Estus Flask+1, goods:194:Ashen Estus Flask+2, goods:196:Ashen Estus Flask+3, goods:198:Ashen Estus Flask+4, goods:200:Ashen Estus Flask+5, goods:202:Ashen Estus Flask+6, goods:204:Ashen Estus Flask+7, goods:206:Ashen Estus Flask+8, goods:208:Ashen Estus Flask+9, goods:210:Ashen Estus Flask+10
        call = t400000_x9005(goods2=150, goods3=1)
        if call.Get() == 1:
            """State 12,9"""
            if GetEstusAllocation(0) + GetEstusAllocation(1) < val1:
                """State 1"""
                # goods:2141:Estus Shard
                if ComparePlayerInventoryNumber(3, goods1, 2, 0, 0) == 1:
                    """State 2,14"""
                    # action:12002003:"Use <?gdsparam@2141?> to reinforce Estus Flask?"
                    call = t400000_x9006(action2=12002003)
                    if call.Get() == 0:
                        """State 4,6"""
                        # goods:2141:Estus Shard
                        PlayerEquipmentQuantityChange(3, goods1, -1)
                        """State 7"""
                        EstusAllocationUpdate(GetEstusAllocation(0) + 1, 0)
                        """State 16"""
                        # action:13002010:"Reinforced Estus Flask, increasing number of uses\n"
                        assert t400000_x9007(action1=13002010)
                        """State 22"""
                        assert t400000_x9008(val2=14)
                    elif call.Done():
                        """State 5"""
                        pass
                else:
                    """State 3,15"""
                    # action:13002011:"No <?gdsparam@2141?> in inventory"
                    assert t400000_x9007(action1=13002011)
            else:
                """State 8,17"""
                # action:13002012:"Cannot reinforce further"
                assert t400000_x9007(action1=13002012)
        elif call.Done():
            """State 13,21"""
            # action:13002014:"No <?gdsparam@190?> in inventory"
            assert t400000_x9007(action1=13002014)
    elif call.Done():
        """State 11,20"""
        # action:13002013:"No <?gdsparam@150?> in inventory"
        assert t400000_x9007(action1=13002013)
    """State 23"""
    return 0

def t400000_x9004(z2=150):
    """State 0,6"""
    # goods:151:Estus Flask, goods:153:Estus Flask+1, goods:155:Estus Flask+2, goods:157:Estus Flask+3, goods:159:Estus Flask+4, goods:161:Estus Flask+5, goods:163:Estus Flask+6, goods:165:Estus Flask+7, goods:167:Estus Flask+8, goods:169:Estus Flask+9, goods:171:Estus Flask+10, goods:150:Estus Flask, goods:152:Estus Flask+1, goods:154:Estus Flask+2, goods:156:Estus Flask+3, goods:158:Estus Flask+4, goods:160:Estus Flask+5, goods:162:Estus Flask+6, goods:164:Estus Flask+7, goods:166:Estus Flask+8, goods:168:Estus Flask+9, goods:170:Estus Flask+10
    call = t400000_x9005(goods2=150, goods3=0)
    if call.Get() == 1:
        """State 1,7"""
        # goods:191:Ashen Estus Flask, goods:193:Ashen Estus Flask+1, goods:195:Ashen Estus Flask+2, goods:197:Ashen Estus Flask+3, goods:199:Ashen Estus Flask+4, goods:201:Ashen Estus Flask+5, goods:203:Ashen Estus Flask+6, goods:205:Ashen Estus Flask+7, goods:207:Ashen Estus Flask+8, goods:209:Ashen Estus Flask+9, goods:211:Ashen Estus Flask+10, goods:190:Ashen Estus Flask, goods:192:Ashen Estus Flask+1, goods:194:Ashen Estus Flask+2, goods:196:Ashen Estus Flask+3, goods:198:Ashen Estus Flask+4, goods:200:Ashen Estus Flask+5, goods:202:Ashen Estus Flask+6, goods:204:Ashen Estus Flask+7, goods:206:Ashen Estus Flask+8, goods:208:Ashen Estus Flask+9, goods:210:Ashen Estus Flask+10
        call = t400000_x9005(goods2=150, goods3=1)
        if call.Get() == 1:
            """State 3,4"""
            OpenEstusAllotMenu()
            assert not (CheckSpecificPersonMenuIsOpen(14, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif call.Done():
            """State 5,9"""
            # action:13002014:"No <?gdsparam@190?> in inventory"
            assert t400000_x9007(action1=13002014)
    elif call.Done():
        """State 2,8"""
        # action:13002013:"No <?gdsparam@150?> in inventory"
        assert t400000_x9007(action1=13002013)
    """State 10"""
    return 0

def t400000_x9005(goods2=150, goods3=_):
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

def t400000_x9006(action2=12002003):
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

def t400000_x9007(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t400000_x9008(val2=14):
    """State 0,3"""
    if GetEstusAllocation(0) + GetEstusAllocation(1) < val2:
        """State 2"""
        pass
    else:
        """State 1,4"""
        RequestUnlockTrophy(16)
    """State 5"""
    return 0

def t400000_x9999():
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
                assert t400000_x9002(action3=13010000)
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
            assert t400000_x9004(z2=150) and not (CheckSpecificPersonMenuIsOpen(8, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 8:
            """State 19,25"""
            # goods:2141:Estus Shard
            assert (t400000_x9003(z1=150, goods1=2141, val1=14) and not (CheckSpecificPersonMenuIsOpen(8,
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

