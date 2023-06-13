# luminae_bot/modules/trivia_module/trivia.py

import random
import asyncio
from ...data.db_utils import (add_asked_question, fetch_asked_questions,
                             update_user_score, fetch_user_score, add_user)

@bot.command()
async def trivia(ctx, category: str):
    conn = create_connection('luminae_bot/data/scores.db')

    # Fetch questions for the category from World Anvil API
    trivia_questions = fetch_trivia_questions(category)

    # Fetch already asked questions for the category
    asked_questions = fetch_asked_questions(conn, category)

    # Exclude already asked questions
    new_questions = [q for q in trivia_questions if q['id'] not in asked_questions]

    # If all questions have been asked, reset the asked questions list
    if not new_questions:
        asked_questions = []
        new_questions = trivia_questions

    # Select a random question
    question = random.choice(new_questions)

    # Ask the question
    await ctx.send(question['text'])

    def check(m):
        return m.content.lower() == question['answer'].lower() and m.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('Sorry, time is up!')
    else:
        # Update user score
        username = msg.author.name
        user_score = fetch_user_score(conn, username, category)
        if user_score is None:
            add_user(conn, username, category)
        update_user_score(conn, username, category)
        await ctx.send(f"Correct answer, {username}! You've earned 1 point.")
        
