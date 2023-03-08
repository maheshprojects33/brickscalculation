from django.shortcuts import render, redirect
from django.contrib import messages
import math

# Create your views here.
# def home(request):
#     context = {}
#     if request.method == 'POST':
#         l = request.POST.get('L')
#         w = request.POST.get('W')
#         h = request.POST.get('H')
#         t = request.POST.get('T')
#         mt = request.POST.get('MT')
        
#         # Size of Windows
#         ww = request.POST.get('WW')
#         wh = request.POST.get('WH')
#         wt = request.POST.get('WT')
#         # 

#         # Size of Doors
#         dw = request.POST.get('DW')
#         dh = request.POST.get('DH')
#         dt = request.POST.get('DT')
#         # 

#         # Size of Bricks
#         bl = request.POST.get('BL')
#         bw = request.POST.get('BW')
#         bh = request.POST.get('BH')
#         wb = request.POST.get('WB')

#         print(t)


#         if t.isdigit()  :
#             length_of_long_wall = float(l) * 2
#             vol_of_long_wall = length_of_long_wall * float(h) * float(t)
            

#             short_wall = float(t) * 2
#             length_of_short_wall = (float(w) - short_wall) * 2
#             vol_of_short_wall = length_of_short_wall * float(h) * float(t)

#             size_of_windows = float(wh) * float(ww) * float(wt)
#             size_window = size_of_windows * float(t)
#             deduction_of_window_ = vol_of_long_wall - size_window
#             deduction_of_window = round(deduction_of_window_, 2)

#             size_of_door = float(dh) * float(dw) * float(dt)
#             size_door = size_of_door * float(t)
#             deduction_of_door_ = vol_of_short_wall - size_door
#             deduction_of_door = round(deduction_of_door_, 2)

#             wastage_of_bricks_ = float(wb) /100
#             wastage_of_bricks = round(wastage_of_bricks_, 2)
            
#             total_vol_ = deduction_of_window + deduction_of_door
#             total_vol = round(total_vol_, 2)

#             blmt = float(bl) + float(mt)
#             bwmt = float(bw) + float(mt)
#             bhmt = float(bh) + float(mt)
#             vol_of_brick = blmt * bwmt * bhmt

#             no_of_bricks = total_vol / vol_of_brick
#             no_of_wastage_bricks_ = no_of_bricks * wastage_of_bricks
#             no_of_wastage_bricks = round(no_of_wastage_bricks_, 2)

#             total_reqd_bricks_ = no_of_bricks + no_of_wastage_bricks
#             total_reqd_bricks = math.ceil(total_reqd_bricks_)

#             context = {"answer": total_reqd_bricks}
        
#         else:
#             print("Error")
#             messages.info(request, "Value Should Be A Number Only and Cannot Be Empty")
    
#     return render(request, "index.html", context)

def home(request):
    context = {}
    if request.method == 'POST':
        ls = request.POST.get('L')
        ws = request.POST.get('W')
        hs = request.POST.get('H')
        ts = request.POST.get('T')
        mts = request.POST.get('MT')
        # Size of Windows
        wws = request.POST.get('WW')
        whs = request.POST.get('WH')
        wts = request.POST.get('WT')
        # Size of Doors
        dhs = request.POST.get('DH')
        dws = request.POST.get('DW')
        dts = request.POST.get('DT')
        # Size of Bricks
        bls = request.POST.get('BL')
        bws = request.POST.get('BW')
        bhs = request.POST.get('BH')
        wbs = request.POST.get('WB')
        try:
            l = round(float(ls), 2)
            w = round(float(ws), 2)
            h = round(float(hs), 2)
            t = round(float(ts), 2)
            mt = round(float(mts), 2)

            ww = round(float(wws), 2)
            wh = round(float(whs), 2)
            wt = round(float(wts), 2)

            dh = round(float(dhs), 2)
            dw= round(float(dws), 2)
            dt = round(float(dts), 2)

            bl = round(float(bls), 2)
            bw = round(float(bws), 2)
            bh = round(float(bhs), 2)
            wb = round(float(wbs), 2)

            length_of_long_wall = l * 2
            vol_of_long_wall = length_of_long_wall * h * t

            size_of_windows = ww * wh *t * wt
            print(ww)
            print(wh)
            print(t)
            print(wt)
            deduction_of_window = vol_of_long_wall - size_of_windows

            # vol_of_long_wall = round(vol_of_long_wall_, 2)

            short_wall = t * 2
            length_of_short_wall = (w - short_wall) * 2
            vol_of_short_wall = length_of_short_wall * h * t


            # deduction_of_window = round(deduction_of_window, 2)

            size_of_door = dh * dw * dt
            size_door = size_of_door * t
            deduction_of_door = vol_of_short_wall - size_door
            # deduction_of_door = round(deduction_of_door, 2)

            wastage_of_bricks_ = wb /100
            wastage_of_bricks = round(wastage_of_bricks_, 2)
            
            total_vol_ = deduction_of_window + deduction_of_door
            total_vol = round(total_vol_, 2)

            blmt = bl + mt
            bwmt = bw + mt
            bhmt = bh + mt
            vol_of_brick = blmt * bwmt * bhmt

            no_of_bricks = total_vol / vol_of_brick
            no_of_wastage_bricks = no_of_bricks * wastage_of_bricks
            # no_of_wastage_bricks = round(no_of_wastage_bricks_, 2)

            total_reqd_bricks_ = no_of_bricks + no_of_wastage_bricks
            total_reqd_bricks = math.ceil(total_reqd_bricks_)


            context = {"answer": total_reqd_bricks}
        except ValueError:
            messages.info(request, "Must be a Number")

        

        

    return render(request, "index.html", context)