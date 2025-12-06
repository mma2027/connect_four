Connect Four — Neural Network + MCTS (AlphaZero Style)
======================================================

This project implements a full Connect Four AI using an AlphaZero-style training pipeline:

- Neural network (policy + value head)
- Monte Carlo Tree Search (MCTS)
- Self-play to build a replay buffer
- AlphaZero loss (policy cross-entropy + value MSE)
- Model generations saved incrementally
- Evaluation against older versions and baselines
- Debugging and visualization tools for NN + MCTS

Everything runs locally in Python with no external ML frameworks.

------------------------------------------------------------
INSTALLATION
------------------------------------------------------------

git clone git@github.com:mma2027/connect_four.git
cd connect_four
pip install -r requirements.txt   (optional)

------------------------------------------------------------
QUICK START
------------------------------------------------------------

Train the model:
    python3 train.py

Play against the AI:
    python3 play_with_model.py

AI vs AI viewer (use ← → to step through moves):
    python3 model_vs_model_viewer.py

Evaluate all saved models:
    python3 evaluate.py

Benchmark final model vs baselines:
    python3 eval_baselines.py

Debug a specific position:
    python3 debug.py

Estimate total training runtime:
    python3 estimate_runtime.py

------------------------------------------------------------
PROJECT STRUCTURE
------------------------------------------------------------

connect_four/
    train.py
    play_with_model.py
    model_vs_model_viewer.py
    evaluate.py
    eval_baselines.py
    estimate_runtime.py
    debug.py
    test_mcts_no_nn.py
    baseline_agents.py
    neural_network.py
    mcts.py
    self_play.py
    engines.py
    helper.py
    models/

------------------------------------------------------------
FILE AND FUNCTION OVERVIEW
------------------------------------------------------------

train.py (AlphaZero training loop)
    train_on_buffer_az(model, buffer, epochs, lr, ...)
        Trains the neural network on the replay buffer.
    simulate(model, sims, temperature, dirichlet)
        Generates one self-play game using NN + MCTS.
    evaluate_models(models)
        Compares model generations.
    save_model(model, filename)
        Saves neural network weights.

play_with_model.py (Human vs AI)
    choose_model()
        Lets you select a saved model.
    human_move(board)
        Gets a legal move from terminal input.
    predict_move(board, model, sims)
        Chooses AI move using MCTS + NN.

model_vs_model_viewer.py (AI vs AI + replay viewer)
    choose_agent(prompt)
        Select Random / Heuristic / NN+MCTS agent.
    simulate_game(agent1, agent2)
        Runs a full game and records states.
    viewer_loop(states)
        Step through the game using arrow keys.

evaluate.py (Model evaluation ladder)
    load_all_models()
        Loads and sorts all model files.
    evaluate_models(models, games_vs_prev, games_vs_random)
        Compares each generation vs previous and vs random.

eval_baselines.py (Baseline benchmarking)
    make_nn_mcts_engine(model)
        Wraps an NN into an MCTS-playing agent.
    run_matchups()
        Runs NN vs Random and NN vs HeuristicMCTS.

estimate_runtime.py (Training runtime estimate)
    benchmark_random_games(n)
        Times warmup random self-play.
    benchmark_nn_mcts_games(n)
        Times NN+MCTS self-play.
    benchmark_training_pass()
        Measures one NN training pass.

debug.py (Detailed NN + MCTS inspection)
    run_debug(board_string)
        Shows NN policy/value output and MCTS search stats.

test_mcts_no_nn.py (MCTS without NN)
    HeuristicMCTS
        Uses win/block heuristics instead of NN priors.

baseline_agents.py (Simple baseline agents)
    RandomAgent
        Chooses a random valid move.
    HeuristicMCTS
        Rollout-based MCTS baseline.

neural_network.py (Neural network model)
    forward_policy_value(vec)
        Outputs (policy[7], value).
    backward_az(...)
        AlphaZero loss and SGD update.
    save(path), load(path)
        Serialize/deserialize model weights.

mcts.py (Core Monte Carlo Tree Search)
    MCTSNode
        Stores visits, prior, value, children.
    MCTS.run(board)
        Performs simulations and returns best move.

self_play.py (Self-play game generator)
    simulate(model, sims, temperature, dirichlet)
        Generates states, MCTS policies, and final winner.

engines.py (Agent wrappers)
    engineR(board)
        Random move engine.
    make_nn_engine(model)
        Pure NN agent.
    make_nn_mcts_engine(model)
        NN+MCTS engine used for training and play.

helper.py (Game utilities)
    create_board()
    get_valid_moves(board)
    drop_piece(board, player, col)
    check_win(board, player)
    is_draw(board)
    board_to_vector(board, player)
    print_board(board)
        Core game logic, state encoding, and display utilities.

------------------------------------------------------------
FUTURE IMPROVEMENTS
------------------------------------------------------------
- GUI interface
- Parallel self-play for faster training
- Larger neural network
- Tournament evaluation mode
- More advanced heuristics for cold-start phase
