
#################################
#                               #
#   Author:  Carlos Luna-Mota   #
#   Version: 2024-07-11         #
#   License: The Unlicense      #
#                               #
#################################

from pyx  import *
from datetime import date, timedelta

### AUXILIARY FUNCTIONS ########################################################
#
def weeks_since(first, last=date.today()):

    middle = date(last.year-1, first.month, first.day)

    return 52*(middle.year-first.year) + (last-middle).days//7
#
def Memento_Mori(YEARS=85, FILL=0, MARGIN=15, COLOR=color.rgb.red):

    # Constants:
    filename = "Memento Mori"
    width    = 21.0 # A4 width
    height   = 29.7 # A4 height

    # Layout:
    K        = 1 + (YEARS-1 + (YEARS-1)//5)*1.5
    size     = min((width - MARGIN/5)/95.5, (height - MARGIN/5)/K)
    x_margin = (width  - 95.5*size)/2
    y_margin = (height -    K*size)/2
    
    # Styles:
    EMPTY  = [style.linecap.round, style.linejoin.round, style.linewidth.Thick]
    FILLED = EMPTY + [deco.filled([COLOR])]
    y_fill = FILL // 52
    w_fill = FILL %  52

    # Setup Drawing:
    CANVAS = canvas.canvas()

    # Draw Squares:
    for y in range(YEARS):

        Y = y_margin + (y + y//5)*1.5*size

        for w in range(52):

            X = x_margin + (w + w//4)*1.5*size
            
            if y_fill > y or (y_fill == y and w_fill > w): STYLE = FILLED
            else:                                          STYLE = EMPTY

            CANVAS.stroke(path.path(path.moveto(X,      -Y     ),
                                    path.lineto(X+size, -Y     ),
                                    path.lineto(X+size, -Y-size),
                                    path.lineto(X,      -Y-size),
                                    path.closepath()),
                                    STYLE)

    # Draw Paper:
    CANVAS.stroke(path.path(path.moveto(      1/20, -1/20       ),
                            path.lineto(      1/20,  1/20-height),
                            path.lineto(width-1/20,  1/20-height),
                            path.lineto(width-1/20, -1/20       ),
                            path.closepath()),
                            EMPTY + [color.rgb.white, style.linewidth.THIN])

    # Output PDF:
    CANVAS.writePDFfile(filename)
#
### MAIN #######################################################################
#
if __name__ == "__main__": Memento_Mori(FILL=weeks_since(date(1985,9,6)))
#    
################################################################################
