<script>
  import InputBox from './lib/InputBox.svelte'
  import ScenarioGen from './lib/ScenarioGen.svelte'
  import '@fontsource/bad-script';

</script>

<main>

  <h1>AiDemise</h1>

  <div class="card">
    <ScenarioGen/>
  </div>

  <div class="card">
    <InputBox/>
  </div>

  <p> Reload the page to play again. ( cnrl + r )</p>
</main>

<style>
  :global(h1, body, textarea, input) {
    font-family: "bad script";
  }
</style>
