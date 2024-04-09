import flwr as fl

NUM_CLIENTS = 10  # Number of clients participating in federated learning
client_resources = {"cpu": 1}  # Define resources for each client, for example

# Define metric aggregation function
def weighted_average(metrics: List[Tuple[int, fl.common.Metrics]]) -> fl.common.Metrics:
    accuracies = [num_examples * m["accuracy"] for num_examples, m in metrics]
    examples = [num_examples for num_examples, _ in metrics]
    return {"accuracy": sum(accuracies) / sum(examples)}

# Create FedAvg strategy
strategy = fl.server.strategy.FedAvg(
    fraction_fit=1.0,
    fraction_evaluate=0.5,
    min_fit_clients=10,
    min_evaluate_clients=5,
    min_available_clients=10,
    evaluate_metrics_aggregation_fn=weighted_average,
)