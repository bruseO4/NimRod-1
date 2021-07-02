import constant
import json
import logit_bias
import openai


def openai_request(request):
    full_request = "Q: HTML for " + request + "\nA:"

    with open('keys.json') as f:
        keys = json.load(f)

    openai.api_key = keys['openapi']

    response = openai.Completion.create(
        prompt=full_request,
        engine=constant.ENGINE,
        max_tokens=constant.MAX_TOKENS,
        frequency_penalty=constant.FREQUENCY_PENALTY,
        logit_bias=logit_bias.logit_bias,
        presence_penalty=constant.PRESENCE_PENALTY,
        temperature=constant.TEMPERATURE,
        top_p=constant.TOP_P,
        stop="\nQ:"
    )

    return response.choices[0].text
