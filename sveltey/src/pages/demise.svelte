<!-- demise.svelte -->
<script>
  import InputBox from "../lib/InputBox.svelte";
  import ScenarioGen from "../lib/ScenarioGen.svelte";
  import "@fontsource/bad-script";
  import { writable } from "svelte/store";

  const sessionId = writable(null);
</script>

<main>
  <h1>AiDemise</h1>
  <div class="card">
    <ScenarioGen {sessionId} />
    <InputBox {sessionId} />
  </div>

  <p>Reload the page to play again. ( ctrl + r )</p>
</main>

<style>
  :global(h1, body, textarea, input) {
    font-family: "bad script";
  }
</style>
