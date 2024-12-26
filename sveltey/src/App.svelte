<script>
  import InputBox from './lib/InputBox.svelte'
  import Counter from './lib/Counter.svelte'
  import '@fontsource/bad-script';

</script>

<main>

  <h1>AiDemise</h1>

  <div class="card">
    <Counter />
  </div>

  <div class="card">
    <InputBox />
  </div>

</main>

<style>
  :global(h1) {
    font-family: "bad script";
  }
</style>
