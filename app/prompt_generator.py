def prepare_final_prompt(prompt, theme, effects, audio_data=None):
    final_prompt = f"{theme.capitalize()} video: {prompt}. "
    if effects:
        final_prompt += f"Include effects: {', '.join(effects)}. "
    if audio_data and "Beat Sync" in effects:
        final_prompt += f"Sync to {audio_data['tempo']} BPM."
    return final_prompt
