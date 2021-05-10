from enum import Enum, auto


class AnswerType(Enum):
    NULL_ANSWER = auto()
    BOOL_ANSWER = auto()
    EXTRACTIVE_ANSWER = auto()
    NUMERIC_ANSWER = auto()
    LIST_ANSWER = auto()
    EMPTY_LIST_ANSWER = auto()


def guess_answer_type(answer, query_type=None):
    if isinstance(answer, str) and answer in {"Yes", "No"}:
        return AnswerType.BOOL_ANSWER
    elif answer == "None":
        return AnswerType.NULL_ANSWER
    elif isinstance(answer, str):
        return AnswerType.EXTRACTIVE_ANSWER
    elif isinstance(answer, int) or query_type == "count":
        return AnswerType.NUMERIC_ANSWER
    elif isinstance(answer, list) or query_type == "list" or query_type == "set":
        if len(answer):
            return AnswerType.LIST_ANSWER
        else:
            return AnswerType.EMPTY_LIST_ANSWER

    raise ValueError("Unable to determine answer type from: {}".format(answer))
