from utils.texttospeech import text_to_speech
from commands import RegexCommand
from config import BALANCE_PATH

class AccountBalanceCommand(RegexCommand):
    """
    Reads the bank account's balance from a file generated by an external script.
    """
    def __init__(self, name='command'):
        """
        Build the basic regex command
        """
        format1_part1 = "(tell me |show me |read me )?"
        format1_part2_v1 = "((what's |what is )?my (bank )?account balance(like)?)"
        format1_part2_v2 = "((what's |what is (there )?|how much (do )?i have |how much (is there |there is ))in my (bank )?account)"
        format1 = "{p1}({p2v1}|{p2v2})".format(
            p1 = format1_part1,
            p2v1 = format1_part2_v1,
            p2v2 = format1_part2_v2,
        )

        format2 = "give me my account balance"

        regex = "({f1}|{f2})".format(
            f1 = format1,
            f2 = format2,
        )

        super(AccountBalanceCommand, self).__init__(regex, True)

    def on_event(self, event, sender):
        """
        Reads the account balance generated by selenium-td.py. The text file
        is a human-readable string.
        """
        if self.match(event['text']):
            try:
                with open(BALANCE_PATH) as file:
                    text = file.read()
                text_to_speech(text)
            except:
                text_to_speech("I am afraid I cannot get your account balance, sorry.")