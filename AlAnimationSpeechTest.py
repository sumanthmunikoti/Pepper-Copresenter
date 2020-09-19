
import qi
import argparse
import sys


def main(session):
    """
    This example uses the run and runTag methods.
    """
    # Get the service ALAnimationPlayer.

    animation_player_service = session.service("ALAnimationPlayer")

    # [posture] will be replaced by Stand, Sit or SitOnPod
    animation_player_service.run("animations/Stand/Gestures/Hey_3")
    # run animation that have the tag "hello"
    animation_player_service.runTag("hello")


if __name__ == "__main__":
    session = qi.Session()
    try:
        session.connect("tcp://127.0.0.1:61305")
    except RuntimeError:
        print ("Can't connect to Naoqi at ip n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)