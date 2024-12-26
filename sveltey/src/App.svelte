<script>
  import InputBox from './lib/InputBox.svelte'
  import '@fontsource/bad-script';

</script>

<main>

  <h1>AiDemise</h1>

  <p class="Saneriao"> The building around you is engulfed in flames, smoke filling the air as the heat intensifies. You must act fast to survive. Your goal is to find a way out before the fire consumes everything. You can search for a fire extinguisher to control the flames or try to find an emergency exit. There may be hidden routes or tools, like a flashlight or water, to help you navigate the smoke and obstacles. But time is running out—the fire spreads quickly, and the building could collapse at any moment.<br><br>What will you do?</p>

  <div class="card">
    <InputBox />
  </div>

</main>

<style>
  :global(h1, body, textarea, input) {
    font-family: "bad script";
  }
</style>
