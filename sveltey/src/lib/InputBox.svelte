<script>
    import { get } from "svelte/store";
    import SuccessMessage from "./SuccessMessage.svelte";
  
    export let sessionId;
    let showMessage = false;
    let userResponse = "";
    let storyResult = null;
    let loading = false;
  
    async function handleSubmit(event) {
      event.preventDefault();
  
      // Get the current value from the sessionId store
      let currentSessionId = get(sessionId);
  
      // Update this check
      if (!currentSessionId) {
        console.error("No session ID available");
        return;
      }
      loading = true;
      try {
        const response = await fetch(
            `https://zz1l696m-8000.uks1.devtunnels.ms/gen_story_result?session_id=${currentSessionId}&user_response=${encodeURIComponent(userResponse)}`
            );
        const data = await response.json();
        if (data.story_result) {
          storyResult = data.story_result;
          showMessage = true;
          setTimeout(() => (showMessage = false), 1000);
        }
      } catch (error) {
        console.error("Error:", error);
      } finally {
        loading = false;
      }
    }
</script>

<div>
    <form on:submit={handleSubmit}>
      <input type="text" bind:value={userResponse} />
      <br /><br />
    
      <button type="submit" disabled={loading}>
        {#if loading}
          <div class="loading"></div>
        {:else}
          Submit
        {/if}
      </button>
    </form>
    <br/>
  
    <SuccessMessage show={showMessage} />
  
    {#if storyResult}
      <div class="story-result">{storyResult.result}</div>
  
      <div class="status-box" class:alive={storyResult.alive} class:dead={!storyResult.alive}>
        {storyResult.alive ? "You Survived!" : "You Died!"}
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
    .loading {
      border: 1px solid #f3f3f3;
      border-radius: 50%;
      border-top: 1px solid #313234;
      width: 20px;
      height: 20px;
      animation: spin 2s linear infinite;
    }
  
    .status-box {
      padding: 10px;
      border-radius: 5px;
      text-align: center;
      margin-top: 10px;
    }
  
    .status-box.alive {
      color: #ffffff;
      background-color: #155724;
    }
  
    .status-box.dead {
      color: #ffffff;
      background-color: #721c24;
    }
  
    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }
  </style>