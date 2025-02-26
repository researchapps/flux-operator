/*
Copyright 2022-2023 Lawrence Livermore National Security, LLC
 (c.f. AUTHORS, NOTICE.LLNS, COPYING)

This is part of the Flux resource manager framework.
For details, see https://github.com/flux-framework.

SPDX-License-Identifier: Apache-2.0
*/

package controllers

import (
	"context"

	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/util/intstr"
	ctrl "sigs.k8s.io/controller-runtime"

	"k8s.io/apimachinery/pkg/api/errors"
	"k8s.io/apimachinery/pkg/types"

	api "flux-framework/flux-operator/api/v1alpha1"
)

var (
	restfulServiceName = "flux-service"
	servicePort        = 5000
)

// exposeService will expose services - one for the port 5000 forward, and the other for job networking (headless)
func (r *MiniClusterReconciler) exposeServices(
	ctx context.Context,
	cluster *api.MiniCluster,
	serviceName string,
	selector map[string]string,
) (ctrl.Result, error) {

	// This service is for the restful API
	existing := &corev1.Service{}
	err := r.Client.Get(ctx, types.NamespacedName{Name: serviceName, Namespace: cluster.Namespace}, existing)
	if err != nil {
		if errors.IsNotFound(err) {
			_, err = r.createHeadlessService(ctx, cluster, serviceName, selector)

		}
		return ctrl.Result{}, err
	}
	return ctrl.Result{}, err
}

// createHeadlessService creates the service for the minicluster
func (r *MiniClusterReconciler) createHeadlessService(
	ctx context.Context,
	cluster *api.MiniCluster,
	serviceName string,
	selector map[string]string,
) (*corev1.Service, error) {

	r.log.Info("Creating headless service with: ", serviceName, cluster.Namespace)
	service := &corev1.Service{
		ObjectMeta: metav1.ObjectMeta{Name: serviceName, Namespace: cluster.Namespace},
		Spec: corev1.ServiceSpec{
			ClusterIP: "None",
			Selector:  selector,
		},
	}
	ctrl.SetControllerReference(cluster, service, r.Scheme)
	err := r.Client.Create(ctx, service)
	if err != nil {
		r.log.Error(err, "🔴 Create service", "Service", service.Name)
	}
	return service, err
}

// exposeService creates a port-specific service for the minicluster
func (r *MiniClusterReconciler) exposeService(
	ctx context.Context,
	cluster *api.MiniCluster,
	serviceName string,
	selector map[string]string,
	ports []int32,
) (ctrl.Result, error) {

	// This service is for the restful API
	existing := &corev1.Service{}
	err := r.Client.Get(ctx, types.NamespacedName{Name: serviceName, Namespace: cluster.Namespace}, existing)
	if err != nil {
		if errors.IsNotFound(err) {
			r.log.Info("Creating service with: ", serviceName, cluster.Namespace)

			// Assemble ports
			servicePorts := []corev1.ServicePort{}
			for _, port := range ports {
				newPort := corev1.ServicePort{
					Protocol: "TCP",

					// This is a very weird parsing... OK
					TargetPort: intstr.FromInt(int(port)),
					Port:       port,
				}
				servicePorts = append(servicePorts, newPort)
			}
			service := &corev1.Service{
				ObjectMeta: metav1.ObjectMeta{Name: serviceName, Namespace: cluster.Namespace},
				Spec: corev1.ServiceSpec{
					Selector: selector,
					Ports:    servicePorts,
				},
			}
			ctrl.SetControllerReference(cluster, service, r.Scheme)
			err := r.Client.Create(ctx, service)
			if err != nil {
				r.log.Error(err, "🔴 Create service", "Service", service.Name)
			}
		}
		return ctrl.Result{}, err
	}
	return ctrl.Result{}, err
}
