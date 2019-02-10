from display import *

def line(img,r0,c0,r1,c1,color):
    if r0>r1:
        start=[r1,c1]
        end=[r0,c0]
    elif r0<r1:
        start=[r0,c0]
        end=[r1,c1]
    elif c0>c1:
        start=[r1,c1]
        end=[r0,c0]
    else:
        start=[r0,c0]
        end=[r1,c1]
    drow=end[0]-start[0]
    dcol=end[1]-start[1]
    if drow==0:
        col=start[1]
        while col<end[1]:
            img[start[0]][col]=color[:]
            col+=1
    else:
        slope=dcol/drow
        if slope>=0 and slope<=1:
            row=start[0]
            col=start[1]
            d=2*dcol-drow
            drow*=2
            dcol*=2
            while(row<=end[0]):
                img[row][col]=color[:]
                #c=((c1-c0)/(r1-r0))(r-r0)+c0
                if d>0:
                    col+=1
                    d-=drow
                row+=1
                d+=dcol
        elif slope>1:
            row=start[0]
            col=start[1]
            d=dcol-2*drow
            drow*=2
            dcol*=2
            while(col<=end[1]):
                img[row][col]=color[:]
                #c=((c1-c0)/(r1-r0))(r-r0)+c0
                if d<0:
                    row+=1
                    d+=dcol
                col+=1
                d-=drow
        elif slope<0 and slope>=-1:
            row=start[0]
            col=start[1]
            d=2*dcol+drow
            drow*=2
            dcol*=2
            while(row<=end[0]):
                img[row][col]=color[:]
                #c=((c1-c0)/(r1-r0))(r-r0)+c0
                if d<0:
                    col-=1
                    d+=drow
                row+=1
                d+=dcol
        elif slope<-1:
            row=start[0]
            col=start[1]
            d=dcol+2*drow
            drow*=2
            dcol*=2
            while(col>=end[1]):
                img[row][col]=color[:]
                #c=((c1-c0)/(r1-r0))(r-r0)+c0
                if d>0:
                    row+=1
                    d+=dcol
                col-=1
                d+=drow
    return img
