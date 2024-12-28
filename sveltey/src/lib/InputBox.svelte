<script>
    import SuccessMessage from './SuccessMessage.svelte';
    let showMessage = false;
    let userResponse = '';
    let storyResult = null;

    async function handleSubmit(event) {
        event.preventDefault();
        const response = await fetch(`http://localhost:8000/gen_story_result?user_response=${encodeURIComponent(userResponse)}`);
        const data = await response.json();
        if (data.story_result) {
            storyResult = data.story_result;
            showMessage = true;
            setTimeout(() => showMessage = false, 1000);
        }
    }
</script>

<div>
    <form on:submit={handleSubmit}>
        <input type="text" bind:value={userResponse} />
        <br><br>
        <button type="submit">Submit</button>
    </form>
    <br>
    <br>
    <SuccessMessage show={showMessage} />
    {#if storyResult}
        <div class="story-result">{storyResult.result}</div>
        <div class="status-box" class:alive={storyResult.alive} class:dead={!storyResult.alive}>
            {storyResult.alive ? 'You Survived!' : 'You Died!'}
        </div>
    {/if}
</div>

<style>
    input {
        border: 2px solid #ccc;
        border-radius: 4px;
        padding: 10px;
        font-size: 16px;
        width: 100%;
        box-sizing: border-box;
    }
    .story-result {
        margin-top: 20px;
        font-family: "bad script";
        font-size: large;
    }
    .status-box {
        margin-top: 15px;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        font-weight: bold;
        color: white;
    }
    .alive {
        background-color: #4CAF50;
    }
    .dead {
        background-color: #f44336;
    }
</style>