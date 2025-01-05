<!-- pvp.svelte -->
<script>
  import { onMount, onDestroy } from 'svelte';
  import '@fontsource/bad-script';
  import SuccessMessage from '../lib/SuccessMessage.svelte';

  let username = '';
  let userResponse = '';
  let scenario = 'Waiting for scenario...';
  let submitted = false;
  let showMessage = false;
  let finalStory = '';
  let loading = false;
  let totalParticipants = 0;
  let currentSubmissions = 0;
  let pollInterval;

  async function joinSession() {
    if (!username) return;
    
    try {
      const response = await fetch(`${import.meta.env.VITE_API_SERVER_ADDRESS}/join_pvp`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username })
      });
      const data = await response.json();
      scenario = data.scenario;
      totalParticipants = data.total_participants;
      startPolling();
    } catch (err) {
      console.error('Error joining session:', err);
    }
  }

  async function submitResponse() {
    if (!userResponse || !username || submitted) return;
    
    loading = true;
    try {
      const response = await fetch(`${import.meta.env.VITE_API_SERVER_ADDRESS}/submit_pvp_response`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username,
          response: userResponse
        })
      });
      const data = await response.json();
      
      if (data.status === 'complete') {
        finalStory = data.story;  // Update to use the new response format
        stopPolling();
      } else {
        currentSubmissions = data.submissions;
      }
      
      submitted = true;
      showMessage = true;
      setTimeout(() => (showMessage = false), 1000);
    } catch (err) {
      console.error('Error submitting response:', err);
    } finally {
      loading = false;
    }
  }

  async function checkStatus() {
    try {
      const response = await fetch(`${import.meta.env.VITE_API_SERVER_ADDRESS}/pvp_status`);
      const data = await response.json();
      scenario = data.scenario || scenario;
      currentSubmissions = data.submissions;
      totalParticipants = data.total;

      if (data.status === 'complete' && data.story) {
        finalStory = data.story;
        stopPolling();
      }
    } catch (err) {
      console.error('Error checking status:', err);
    }
  }

  function startPolling() {
    pollInterval = setInterval(checkStatus, 2000);
  }

  function stopPolling() {
    if (pollInterval) {
      clearInterval(pollInterval);
    }
  }

  onMount(() => {
    if (username) {
      joinSession();
    }
  });

  onDestroy(() => {
    stopPolling();
  });
</script>

<main>
  <h1>AiDemise PvP</h1>

  <div class="card">
    <div class="join-section">
      <label for="username">Username:</label>
      <br />
      <input type="text" id="username" bind:value={username} />
      <br /> <br />
      <button on:click={joinSession}>Join Session</button>
    </div>

    <p class="scenario">{scenario}</p>

    <form on:submit|preventDefault={() => submitResponse()}>
      <textarea 
        bind:value={userResponse} 
        placeholder="Your response..." 
        disabled={submitted}
      ></textarea>
      <button type="submit" disabled={loading || submitted}>
        {loading ? 'Submitting...' : 'Submit'}
      </button>
    </form>

    {#if showMessage}
      <SuccessMessage show={showMessage} />
    {/if}

    {#if submitted && !finalStory}
      <div class="status">
        Waiting for other players... ({currentSubmissions}/{totalParticipants})
      </div>
    {/if}

    {#if finalStory}
      <div class="final-story">
        <h2>Final Story</h2>
        <p>{finalStory}</p>
      </div>
    {/if}
  </div>
  <p> Reload the page to play again. ( ctrl + r )</p>
</main>

<style>
  :global(h1, body, textarea, input) {
    font-family: "bad script";
  }

  .card {
    padding: 2em;
    max-width: 800px;
    margin: 0 auto;
  }

  .join-section {
    margin-bottom: 1em;
  }

  .scenario {
    margin: 1em 0;
    font-size: 1.1em;
  }

  textarea {
    width: 100%;
    min-height: 150px;
    margin: 1em 0;
    padding: 0.5em;
  }

  .status {
    margin-top: 1em;
    color: #666;
    font-style: italic;
  }

  .final-story {
    margin-top: 2em;
    padding: 1em;
    border-radius: 4px;
  }
</style>
