import pygame
import sys

pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((500,500))
pygame.display.set_caption ("Countdown Timer")

BLUE_GRAY= (105, 157, 196)
HARVEST_GOLD = (252, 194, 0)
BLACK = (0,0,0)
RED = (255, 0, 0)
font = pygame.font.Font(None, 36)


#load alarm sound
total_seconds = 0
alarm_on = False
alarm_sound = pygame.mixer.Sound("Song_Rest _In_ Peace.mp3")

# Initial time settings (minutes and seconds)
minutes = 0
seconds = 0
counting_down = False

# Helper to render text centered in a rect
def draw_text_center(text, font, color, surface, rect):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center = rect.center)
    surface.blit(text_surf, text_rect)

# Rectangle for buttons
BTN_MIN_PLUS = pygame.Rect(100, 50, 50, 50)
BTN_MIN_MINUS = pygame.Rect(100, 150, 50, 50)
BTN_SEC_PLUS = pygame.Rect(200, 50, 50, 50)
BTN_SEC_MINUS = pygame.Rect(200, 150, 50, 50)
BTN_START = pygame.Rect(300, 50, 150, 50)
BTN_RESET = pygame.Rect(300, 150, 150, 50)

clock = pygame.time.Clock()
#custom events
timer_event = pygame.USEREVENT + 1 # Custom event for timer tick
alarm_stop_event = pygame.USEREVENT + 2 #stop alarm sound after 30 seconds


while True :
    screen.fill(BLUE_GRAY)
   
    #Draw buttons
    pygame.draw.rect(screen, HARVEST_GOLD, BTN_MIN_PLUS)
    pygame.draw.rect(screen, HARVEST_GOLD, BTN_MIN_MINUS)
    pygame.draw.rect(screen, HARVEST_GOLD, BTN_SEC_PLUS)
    pygame.draw.rect(screen, HARVEST_GOLD, BTN_SEC_MINUS)
    pygame.draw.rect(screen, HARVEST_GOLD, BTN_START)
    pygame.draw.rect(screen, HARVEST_GOLD, BTN_RESET)

    # Draw button labels
    draw_text_center("+", font, BLACK, screen, BTN_MIN_PLUS)
    draw_text_center("-", font, BLACK, screen, BTN_MIN_MINUS)
    draw_text_center("+", font, BLACK, screen, BTN_SEC_PLUS)
    draw_text_center("-", font, BLACK, screen, BTN_SEC_MINUS)
    draw_text_center("Start", font, BLACK, screen, BTN_START)
    draw_text_center("Reset", font, BLACK, screen, BTN_RESET)

    #Draw the clock face
    pygame.draw.circle(screen, BLACK, (150,320), 82)
    pygame.draw.circle(screen, HARVEST_GOLD, (150,320), 80)
    pygame.draw.circle(screen, BLACK, (350,320), 82)
    pygame.draw.circle(screen, HARVEST_GOLD, (350,320), 80)

    #Draw the clock lines
    pygame.draw.circle(screen, BLACK, (350, 320), 5)
    pygame.draw.line(screen, BLACK, (350,320), (350, 250))

    #calculate current total seconds left
    current_time = minutes * 60 +seconds

    #calculate width of the red countdown bar based on time
    if total_seconds > 0:
        bar_width = int(300 * current_time / total_seconds)
    else:
        bar_width = 0

    #Draw the countdown rectangle
    pygame.draw.rect(screen, BLACK, (100, 440, 304,34))
    pygame.draw.rect(screen, HARVEST_GOLD, (102, 442, 300,30))
    pygame.draw.rect(screen, RED, (102, 442, bar_width, 30))

    

    #Display the current time in MM:SS format
    time_str = f"{minutes:02d}:{seconds:02d}"
    time_text = font.render(time_str, True, BLACK)
    time_rect = time_text.get_rect(center=(150,320))
    screen.blit(time_text, time_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if alarm_on:
                alarm_sound.stop()
                pygame.time.set_timer(alarm_stop_event, 0)
                alarm_on = False
            else:
                mouse_pos = event.pos
                if BTN_MIN_PLUS.collidepoint(mouse_pos) and not counting_down:
                    minutes = min(minutes +1, 90) # Limit max to 90 minutes
                    total_seconds = minutes * 60 + seconds 
                elif BTN_MIN_MINUS.collidepoint(mouse_pos) and not counting_down:
                    minutes = max(minutes - 1, 0)
                    total_seconds = minutes * 60 + seconds
                elif BTN_SEC_PLUS.collidepoint(mouse_pos) and not counting_down:
                    if seconds == 59:
                        if minutes <90:
                            minutes += 1
                            seconds = 0
                        else:
                            seconds = 59
                    else:
                        seconds = min(seconds + 1, 59)
                    total_seconds = minutes * 60 + seconds
                elif BTN_SEC_MINUS.collidepoint(mouse_pos) and not counting_down:
                    if seconds == 0:
                        if minutes > 0:
                            minutes -= 1
                            seconds = 59
                        else:
                            seconds = 0
                    else: 
                        seconds = max(seconds - 1, 0)
                    total_seconds = minutes * 60 + seconds
                elif BTN_START.collidepoint(mouse_pos) and not counting_down:
                    if minutes > 0 or seconds > 0:
                        counting_down = True
                        total_seconds = minutes * 60 + seconds # Save total seconds at countdown start
                        pygame.time.set_timer(timer_event, 1000) # set timer to tick every second
                elif BTN_RESET.collidepoint(mouse_pos):
                    counting_down = False
                    pygame.time.set_timer(timer_event, 0)
                    minutes, seconds = 0, 0
                    total_seconds = 0
        
        elif event.type == timer_event and counting_down:
            #count down logic
            if seconds == 0:
                if minutes == 0:
                    counting_down = False
                    pygame.time.set_timer(timer_event, 0)
                    alarm_sound.play()
                    alarm_on = True
                    pygame.time.set_timer(alarm_stop_event, 6000000)
                else:
                    minutes -= 1
                    seconds = 59
            else:
                seconds -= 1
        elif event.type == alarm_stop_event:
            alarm_sound.stop()
            pygame.time.set_timer(alarm_stop_event, 0)
            alarm_on = False
        
    pygame.display.flip()
    clock.tick(30)  # Limit to 30 FPS